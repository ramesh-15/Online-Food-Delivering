from django.shortcuts import render,HttpResponseRedirect
from .forms import logform,regform,userform,donateform,contactform,NGO_request
from .models import Users_donations,Contact,food_requests
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .serializers import FoodSerializer
from django.conf import settings
from django.core.mail import send_mail
from .serializers import UserSeriliazer
from .models import User
from django.contrib import messages
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
def register(request):
    if request.method == 'POST':
        f = regform(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect('/login')
        else:
            return render(request,'reg.html',{'data':f})
    else:
        f = regform()
        return render(request,'reg.html',{'data':f})
def loginview(request):
    if request.method == 'POST':
        f = logform(request.POST)
        if f.is_valid():
            fname = f.cleaned_data['username']
            fpwd = f.cleaned_data['password']
            user = authenticate(request,username = fname ,password = fpwd)
            if user is not None:
                login(request,user)
                if user.is_Donar:
                    return HttpResponseRedirect('/donar_home')
                elif user.is_NGO:
                    return HttpResponseRedirect('/NGO_home')


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
            fpic = f.cleaned_data['food_pick_up']
            fpin = f.cleaned_data['pincode']

            
              #smtp
            data = User.objects.get(username=request.user)
            stu = UserSeriliazer(data)
            fmail=stu.data['email']
            print(fmail)
            user = Users_donations(donarMail = fmail,food_name=fname,food_type = ftype,quantity = fqty, donar_contact = fcont,food_pick_up = fpic,pincode = fpin)
            user.save()
            subject = 'Waste Food Management System '
            message = f' Hi {request.user} thanks for donating food on Waste Food Management System...'
            sender = settings.EMAIL_HOST_USER
            send_mail(subject, message, sender, [fmail])

            return HttpResponseRedirect('/donar_home')
    else:
        f = donateform()
    return render(request,'donatefood.html',{'data':f})

def DonarCart(request):
    data = Users_donations.objects.all()
    return render(request,'DonarCart.html',{'data':data})

def DonarCancel(request,id):
    data = Users_donations.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/DonarCart')


#  view food of NGO

def NGOrequest(request,id):
    print(id)
    fg = Users_donations.objects.get(id=id)
    print(fg)
    print(fg.flag)
    fg.flag =True
    print(fg.flag)
    fg.save()
    fg = Users_donations.objects.get(id=id)
    stu2= FoodSerializer(fg)
    # print(stu2.data)
    data = User.objects.get(username=request.user)
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
    print(request.user)
    data = Users_donations.objects.filter(flag=True)
    print(data)
    return render(request,'NGO_cart.html',{'data':data})

def NGOCancel(request,id):
    dt = Users_donations.objects.get(id = id)
    # print(dt.food_id)
    dt.flag=False
    dt.save()
    return HttpResponseRedirect('/Cart_NGO')







