from django.shortcuts import render
from .sign_up_form import SignUpForm
from .user_profile_form import UserProfileForm
from .login_form import LoginForm
from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages


def base(request):
    return render(request,'Chat_Mingle/base.html')


# SIGN UP USER
def sign_up(request):
    if request.method == "POST":
        sign_up_form = SignUpForm(request.POST)
        user_profile_form = UserProfileForm(request.POST, request.FILES)

        if sign_up_form.is_valid() and user_profile_form.is_valid():
            user = sign_up_form.save()  # Save the User instance
            profile_form = user_profile_form.save(commit=False)
            profile_form.user = user  # Associate UserProfile with the User
            profile_form.save()  # Save the UserProfile instance
            return redirect('base')  # Redirect to the user's profile page after registration
    else:
        sign_up_form = SignUpForm()
        user_profile_form = UserProfileForm()

    context = {
        'sign_up_form': sign_up_form,
        'user_profile_form': user_profile_form,
    }

    return render(request, 'Chat_Mingle/sign_up_template.html', context)



def chit_chat(request):
    return render(request,'Chat_Mingle/Chit_Chat.html')


# LOGIN USER

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        try:
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, f"Welcome, {username}! You have successfully logged in.")
                    return redirect('base')  # Replace 'home' with your actual home page URL
                else:
                    raise forms.ValidationError("Invalid username or password.")
        except forms.ValidationError as e:
            messages.error(request, str(e))
    else:
        form = LoginForm()

    return render(request, 'Chat_Mingle/login.html', {'login_form': form})



