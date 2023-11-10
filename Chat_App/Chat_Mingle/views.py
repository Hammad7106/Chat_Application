from django.shortcuts import render
from .sign_up_form import SignUpForm
from .user_profile_form import UserProfileForm

from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib import messages


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
