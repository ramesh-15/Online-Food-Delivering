from django.shortcuts import render, HttpResponseRedirect
from .forms import DonarUserForm, Donarlogform
from django.core.mail import send_mail
from django.conf import settings
from .models import DonarUser
from django.contrib.auth import authenticate, login
import random
import string

# Create your views here.

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def passcode():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(6))
    print("Random password is:", password)
    return password

def DonarSignup(request):
    if request.method == 'POST':
        f = DonarUserForm(request.POST)
        if f.is_valid():
            fn = f.cleaned_data['first_name']
            fl = f.cleaned_data['last_name']
            fu = f.cleaned_data['username']
            fem = f.cleaned_data['email']
            fcity = f.cleaned_data['city']
            fstate = f.cleaned_data['state']
            data = DonarUser(first_name = fn,last_name = fl,username = fu,email = fem,passcode = passcode(),city = fcity, state = fstate)
            data.save()
            # smtp passcode
            subject = 'Passcode Varification code '
            message = f' Hi {request.user} thanks for Registering Country Welfare...'
            sender = settings.EMAIL_HOST_USER
            send_mail(subject, message, sender, [fem])
            return HttpResponseRedirect('/log')
        else:
            return render(request, 'signup.html', {'data': f})
    else:
        f = DonarUserForm()
        return render(request, 'signup.html', {'data': f})

def Donarlog(request):
    if request.method == 'POST':
        f = Donarlogform(request.POST)
        if f.is_valid():
            fname = f.cleaned_data['username']
            fpwd = f.cleaned_data['passcode']
            user = DonarUser.objects.get(username=fname, passcode=fpwd)
            print(user)
            if user is not None:
                # login(request, user)
                return HttpResponseRedirect('/home')
            else:
                f = Donarlogform()
                return render(request, 'login.html', {'data': f})
        else:
            f = Donarlogform()
            return render(request, 'login.html', {'data': f})

    else:
        f = Donarlogform()
        return render(request,'login.html',{'data':f})
    
