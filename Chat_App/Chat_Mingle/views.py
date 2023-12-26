from django.shortcuts import render
from .sign_up_form import SignUpForm
from .user_profile_form import UserProfileForm
from .login_form import LoginForm
from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from .models import Group,Chat
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
        try:
            form = LoginForm(request, request.POST)
            if form.is_valid():
                # Authentication successful, log the user in
                user = form.get_user()
                login(request, user)

                # Add a success message
                messages.success(request, f"Welcome, {user.username}! You have successfully logged in.")

                # Redirect to a success page, e.g., dashboard
                return redirect('chit_chat')
        except Exception as e:
            # Handle exceptions (e.g., form validation errors, authentication failures)
            messages.error(request, f"Login failed: {str(e)}")
    else:
        form = LoginForm()

    return render(request, 'Chat_Mingle/login.html', {'login_form':form})


def rooms_list(request):
    return render(request,"Chat_Mingle/enter_room.html")

def room(request, room_name):
    group=Group.objects.filter(name=room_name).first()
    chats = []
    if group:
        chats=Chat.objects.filter(group=group)
    else:
        group=Group(name=room_name)
        group.save()
    return render(request, "Chat_Mingle/room.html", {"room_name": room_name,"chats":chats})

def user_logout(reqeust):
    logout(reqeust)

    return redirect('base')
