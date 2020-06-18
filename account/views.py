from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpRequest
# Create your views here.

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = auth.authenticate(username=username, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def Rform(request):

    if request.method == 'POST':
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        username = request.POST['username']
        password1 = request.POST['password1']
        Pass2 = request.POST['Pass2']
        email = request.POST['email']
        if (Fname==None or Lname==None or username == None or password1 == None or Pass2 == None or email== None):
            messages.info(request, 'Field is Empty')
            return redirect('Rform')
        if password1 == Pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User taken')
                return redirect('Rform')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('Rform')

            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=Fname, last_name=Lname)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'Password must be same')
            return redirect('Rform')
        return redirect('/')
    else:
        return render(request, 'Rform.html')

def logout (request):
    auth.logout(request)
    return redirect('/')