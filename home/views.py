from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator

def home(request):
    return render(request, 'index.html')

def signIn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        if not email or not password:
            messages.error(request, 'Please fill in all fields.')
            return redirect('home:signin')
            
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('admindashboard:adminPage')
        else:
            messages.error(request, 'Invalid details')
            return redirect('home:signin')
    
    return render(request, 'signIn.html')

def signUp(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        
        
        if name == '' or email == '' or password == '':
            messages.error(request, '*All fields are required.')
            return redirect('home:signUp')
        
        if len(password) < 8:
            messages.error(request, 'Password must be 8 characters long.')
            return redirect('home:signUp')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('home:signUp')
        
        else:
            
            myuser = User.objects.create_user(name, email, password)
            myuser.save()
            
            messages.success(request, 'Your account has been created successfully.')           
               
    return render(request, 'signUp.html')


def forgetPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = request.build_absolute_uri(reverse('home:resetPassword', kwargs={'uidb64': uid, 'token': token}))
            context = {'reset_link': reset_link}
            return render(request, 'forgetPassword.html', context)
        except User.DoesNotExist:
            messages.error(request, 'email does not exist')
            return redirect('home:forgetPassword')
    return render(request, 'forgetPassword.html')

def resetPassword(request, uidb64, token):
    if request.method == 'POST':
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect(request.path)
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                user.set_password(pass1)
                user.save()
                messages.success(request, "Password reset successfully")
                return redirect('home:signin')
            else:
                messages.error(request, "Invalid token")
                return redirect('hpme:forgetPassword')
        except User.DoesNotExist:
            messages.error(request, "Invalid user")
            return redirect('home:forgetPassword')
    return render(request, 'resetPassword.html')