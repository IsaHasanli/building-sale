from django.shortcuts import render, redirect
from django.contrib import messages

from account.email import activateEmail
from .forms import RegisterForm 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model,login,logout,authenticate
from .tokens import account_activation_token

User = get_user_model()

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')
    return redirect('blog')

def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            username = User.objects.get(email = email).username
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return redirect("home")
        except:
            messages.error(request,"Email or password not correct")
    return render(request, 'login.html')

def user_logout(request):
    if not request.user.is_authenticated:
        return redirect("home")
    logout(request)
    return redirect("blog")

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('home')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = RegisterForm()

    return render(
        request=request,
        template_name="register.html",
        context={"form": form}
        )