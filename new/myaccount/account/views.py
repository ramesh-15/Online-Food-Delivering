from django.shortcuts import render,HttpResponseRedirect
from .forms import logform,regform,userform,donateform,contactform,NGO_request
from .models import Users_donations,Contact,food_requests
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .serializers import FoodSerializer
# Create your views here.
def donar_home(request):
    return render(request,'Donar_home.html')
def NGO_home(request):
    data = Users_donations.objects.all()
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
            user = Users_donations(food_name=fname,food_type = ftype,quantity = fqty, donar_contact = fcont,food_pick_up = fpic,pincode = fpin)
            user.save()
            return HttpResponseRedirect('/donar_home')
    else:
        f = donateform()
        return render(request,'donatefood.html',{'data':f})
#  view food of NGO

def NGOrequest(request,id):
    data = Users_donations.objects.get(id=id)
    stu = FoodSerializer(data)
    print(stu.data)
    print(stu.data['food_name'])


    var = {
        'id':id,
        'username':request.user,
        'food_items':stu.data['food_name'],
        'pickup_point':stu.data['food_pick_up'],
        'donar_contact':stu.data['donar_contact']
        
    }
    if request.method==('POST' ):
        fm = NGO_request(request.POST or None)
        if fm.is_valid():
            exist = food_requests.objects.filter(id = id)
            print(exist)
            
            if not exist:
                messages.success(request,'requested Successfully... ')
                fm.save()
                dele = Users_donations.objects.get(id=id)
                dele.delete()
                return HttpResponseRedirect('/NGO_home')
            else:
                messages.error(request,'already requested...')
                return render(request,'NGO_request.html',{'data':fm})
    else:
        fm = NGO_request(var)
        return render(request,'NGO_request.html',{'data':fm})

# NGO_ view request

def Cart_NGO(request):
    data = food_requests.objects.filter(username=request.user)
    return render(request,'NGO_cart.html',{'data':data})

def Cancel_NGO(request,id):
    dt = food_requests.objects.filter(id = id)
    # print(dt.food_id)
    dt.delete()
    return HttpResponseRedirect('/Cart_NGO')





