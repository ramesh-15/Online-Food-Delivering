from django.shortcuts import render,HttpResponseRedirect
from .forms import logform,regform,userform,donateform,contactform,ClothesForm,HealthForm,FootwareForm
from .models import Users_donations,Contact,Clothes,Health,Footware,DonarUser
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .serializers import FoodSerializer
from django.conf import settings
from django.core.mail import send_mail
from .serializers import UserSeriliazer
from .models import DonarUser
from django.contrib import messages
from django.db.models import Q
import random
import string
# Create your views here.
def donar_home(request):
    return render(request,'Donar_home.html')
def NGO_home(request):
    data = Users_donations.objects.filter(flag=False)
    return render(request, 'NGO_home.html', {'data': data})

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == 'POST':
        fm = contactform(request.POST)
        if fm.is_valid():
            fname = fm.cleaned_data['name']
            fmail = fm.cleaned_data['email']
            fphone = fm.cleaned_data['phone']
            fsub = fm.cleaned_data['subject']
            fmsg = fm.cleaned_data['message']
            user = Contact(name = fname, email = fmail, phone = fphone, subject = fsub, message = fmsg)
            user.save()
            return HttpResponseRedirect('/home')
        else:
            return render(request,'contact.html',{'data':fm})
    else:
        fm = contactform()
        return render(request,'contact.html',{'data':fm})

def passcode():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(6))
    print("Random password is:", password)
    return password


def DonarSignup(request):
    if request.method == 'POST':
        f = regform(request.POST)
        if f.is_valid():
            fn = f.cleaned_data['first_name']
            fl = f.cleaned_data['last_name']
            fu = f.cleaned_data['username']
            fem = f.cleaned_data['email']
            
            data = DonarUser(first_name = fn,last_name = fl,username = fu,email = fem,passcode = passcode())
            data.save()
            # smtp passcode
            subject = 'Passcode Varification code '
            message = f' Hi {request.user} your passcode : {passcode()}thanks for Registering Country Welfare...'
            sender = settings.EMAIL_HOST_USER
            send_mail(subject, message, sender, [fem])
            return HttpResponseRedirect('/login')
        else:
            return render(request, 'reg.html', {'data': f})
    else:
        f = regform()
        return render(request, 'reg.html', {'data': f})

def Donarlog(request):
    if request.method == 'POST':
        f = logform(request.POST)
        if f.is_valid():
            fname = f.cleaned_data['username']
            fpwd = f.cleaned_data['passcode']
            user = DonarUser.objects.filter(username=fname, passcode=fpwd)
            print(user)
            if user is not None:
                # login(request, user)
                return HttpResponseRedirect('/donar_home')
            else:
                f = logform()
                return render(request, 'log.html', {'data': f})
        else:
            f = logform()
            return render(request, 'log.html', {'data': f})

    else:
        f = logform()
        return render(request,'log.html',{'data':f})

def logoutpage(request):
    logout(request)
    return render(request,'home.html')

def setpwd(request):

    if request.method == "POST":
        print(request.user)
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request, 'Password Changed Successfully')
            return HttpResponseRedirect('/login')
        else:
            return render(request, 'changepwd.html', {'data': fm})
    else:
        fm = PasswordChangeForm(user=request.user)
        return render(request, 'changepwd.html', {'data': fm})

def edituser(request):
    if request.method == 'POST':
        f = userform(request.POST,instance=request.user)
        if f.is_valid():
            f.save()
            if request.user.is_Donar:
                return HttpResponseRedirect('/donar_home')
            elif request.user.is_NGO:
                return HttpResponseRedirect('/NGO_home')
    else:
        f = userform(instance=request.user)
        return render(request,'editprofile.html',{'data':f})

# donate food
def donatefood(request):
    if request.method == 'POST':
        f = donateform(request.POST)

        if f.is_valid():
            fname = f.cleaned_data['food_name']
            ftype = f.cleaned_data['food_type']
            fqty = f.cleaned_data['quantity']
            fcont = f.cleaned_data['donar_contact']
            fpic = f.cleaned_data['pick_up']
            fpin = f.cleaned_data['pincode']

            
              #smtp
            print(request.user)
            data = DonarUser.objects.get(username=request.user)
            print(data)
            stu = UserSeriliazer(data)
            print(stu.data)
            fmail=stu.data['email']
            print(fmail)
            donar_name = stu.data['username']
            user = Users_donations(donar_name =donar_name ,donarMail = fmail,food_name=fname,food_type = ftype,quantity = fqty, donar_contact = fcont,food_pick_up = fpic,pincode = fpin)
            user.save()
            # data = User.objects.get(username=request.user)
            # stu = UserSeriliazer(data)
            # Users_donations.donar_name=stu.data['username']
            # Users_donations.save()
            subject = 'Waste Food Management System '
            message = f' Hi {request.user} thanks for donating food on Waste Food Management System...'
            sender = settings.EMAIL_HOST_USER
            send_mail(subject, message, sender, [fmail])

            return HttpResponseRedirect('/donar_home')
    else:
        f = donateform()
    return render(request,'donatefood.html',{'data':f})

def DonarCart(request):
    food = Users_donations.objects.filter( Q(donar_name = request.user) & (Q(flag = True ) | Q(flag = False)))
    clothes = Clothes.objects.filter( Q(donar_name = request.user) & (Q(flag = True ) | Q(flag = False)))
    health = Health.objects.filter( Q(donar_name = request.user) & (Q(flag = True ) | Q(flag = False)))
    footware = Footware.objects.filter( Q(donar_name = request.user) & (Q(flag = True ) | Q(flag = False)))
    return render(request,'DonarCart.html',{'food':food,'clothes':clothes,'health':health,'footware':footware})

def DonarCancel(request,id):
    food = Users_donations.objects.get(id=id)
    food.delete()  
    return HttpResponseRedirect('/DonarCart')
def DonarRequest(request):
    data = Users_donations.objects.filter(Q(donar_name = request.user) & Q(flag = True))
    return  render(request, 'DonarRequest.html',{'data':data})

def DonarAccept(request,id):
    data = Users_donations.objects.get(id = id)
    data.ngomessage=f'Your food request accepted by donar, proceed to collect the food !!!'
    data.flagreq=True
    data.save()
    return HttpResponseRedirect('/DonarRequest')


def Decline(request,id):
    data = Users_donations.objects.get(id=id)
    data.ngomessage=f'Your food request has declined by donar !!!'
    data.flagreq=False
    data.flag=False
    data.save()
    
    return HttpResponseRedirect('/DonarRequest')

# clothes Donate
def donateclothes(request):
    if request.method == 'POST':
        f = ClothesForm(request.POST)

        if f.is_valid():
            fname = f.cleaned_data['Name']
            ftype = f.cleaned_data['catogiry']
            fqty = f.cleaned_data['pairs']
            fcont = f.cleaned_data['donar_contact']
            fpic = f.cleaned_data['pick_up']
            fpin = f.cleaned_data['pincode']

            
              #smtp
            data = DonarUser.objects.get(username=request.user)
            stu = UserSeriliazer(data)
            fmail=stu.data['email']
            print(fmail)
            donar_name = stu.data['username']
            user = Clothes(donar_name =donar_name ,donarMail = fmail,Name=fname,catogiry = ftype,pairs = fqty, donar_contact = fcont,food_pick_up = fpic,pincode = fpin)
            user.save()
            # data = User.objects.get(username=request.user)
            # stu = UserSeriliazer(data)
            # Users_donations.donar_name=stu.data['username']
            # Users_donations.save()
            subject = 'FeedHunger '
            message = f' Hi {request.user} thanks for donating clothes on Waste FeedHunger application...'
            sender = settings.EMAIL_HOST_USER
            send_mail(subject, message, sender, [fmail])

            return HttpResponseRedirect('/donar_home')
    else:
        f = ClothesForm()
    return render(request,'clothesdonate.html',{'data':f})

def ClothesCancel(request,id):
    clothes = Clothes.objects.get(id=id)
    clothes.delete()
    return HttpResponseRedirect('/DonarCart')

# Charity for Health
def donatehealth(request):
    if request.method == 'POST':
        f = HealthForm(request.POST)

        if f.is_valid():
            fname = f.cleaned_data['drugname']
            ftype = f.cleaned_data['catogiry']
            fqty = f.cleaned_data['quantity']
            fcont = f.cleaned_data['donar_contact']
            fpic = f.cleaned_data['pick_up']
            fpin = f.cleaned_data['pincode']
              #smtp
            data = DonarUser.objects.get(username=request.user)
            stu = UserSeriliazer(data)
            fmail=stu.data['email']
            print(fmail)
            donar_name = stu.data['username']
            user = Health(donar_name =donar_name ,donarMail = fmail,drugname=fname,catogiry = ftype,quantity = fqty, donar_contact = fcont,food_pick_up = fpic,pincode = fpin)
            user.save()
            subject = 'FeedHunger'
            message = f' Hi {request.user} thanks for donating clothes on Waste FeedHunger application...'
            sender = settings.EMAIL_HOST_USER
            send_mail(subject, message, sender, [fmail])
            return HttpResponseRedirect('/donar_home')
    else:
        f = HealthForm()
    return render(request,'healthdonate.html',{'health':f})

def HealthCancel(request,id):
    health = Health.objects.get(id=id)
    health.delete()
    return HttpResponseRedirect('/DonarCart')

# Donate Footware
def donatefootware(request):
    if request.method == 'POST':
        f = FootwareForm(request.POST)

        if f.is_valid():
            fname = f.cleaned_data['name']
            ftype = f.cleaned_data['catogiry']
            fqty = f.cleaned_data['pairs']
            fcont = f.cleaned_data['donar_contact']
            fpic = f.cleaned_data['pick_up']
            fpin = f.cleaned_data['pincode']
              #smtp
            data = DonarUser.objects.get(username=request.user)
            stu = UserSeriliazer(data)
            fmail=stu.data['email']
            print(fmail)
            donar_name = stu.data['username']
            user = Footware(donar_name =donar_name ,donarMail = fmail,name=fname,catogiry = ftype,pairs = fqty, donar_contact = fcont,food_pick_up = fpic,pincode = fpin)
            user.save()
            subject = 'FeedHunger'
            message = f' Hi {request.user} thanks for donating clothes on Waste FeedHunger application...'
            sender = settings.EMAIL_HOST_USER
            send_mail(subject, message, sender, [fmail])
            return HttpResponseRedirect('/donar_home')
    else:
        f = FootwareForm()
    return render(request,'footwaredonate.html',{'health':f})

def FootwareCancel(request,id):
    footware = Footware.objects.get(id=id)
    footware.delete()
    return HttpResponseRedirect('/DonarCart')
#  view food of NGO

def NGOrequest(request,id):
    print(id)
    fg = Users_donations.objects.get(id=id)
    print(fg)
    print(fg.flag)
    fg.flag =True
    print(fg.flag)
    data = DonarUser.objects.get(username=request.user)
    stu = UserSeriliazer(data)
    fg.ngo_name=stu.data['username']
    ngoname=request.user 
    fg.message=f'Your food is requested by {ngoname} with food id ={id}'
    fg.save()
    fg = Users_donations.objects.get(id=id)
    stu2= FoodSerializer(fg)
    # print(stu2.data)
    data = DonarUser.objects.get(username=request.user)
    stu = UserSeriliazer(data)
    print(stu.data)
    fmail=stu.data['email']
    fdonarmail = stu2.data['donarMail']
    print(fdonarmail)
    subject = 'Waste Food Management System '
    message = f' Hi {request.user} thanks for Requesting  food on Waste Food Management System...'
    sender = settings.EMAIL_HOST_USER
    # send_mail(subject, message, sender, [fmail])
    # donar mail
    subject = 'Waste Food Management System '
    message = f' your Food Requested by  {request.user} on Waste Food Management System...'
    sender = settings.EMAIL_HOST_USER
    send_mail(subject, message, sender, [fdonarmail])

    return HttpResponseRedirect('/NGO_home')

# NGO_ view request

def Cart_NGO(request):
    print(request.user)  #Q(name='John') | Q(age=25)
    data = Users_donations.objects.filter(Q(ngo_name = request.user) & Q(flag = True))
    print(data)
    return render(request,'NGO_cart.html',{'data':data})

def NGOCancel(request,id):
    dt = Users_donations.objects.get(id = id)
    # print(dt.food_id)
    dt.flag=False
    dt.save()
    return HttpResponseRedirect('/Cart_NGO')
def NGORequest(request):
    data = Users_donations.objects.filter(Q(ngo_name = request.user) & Q(flag = True))
    return  render(request, 'NGORequest.html',{'data':data})






