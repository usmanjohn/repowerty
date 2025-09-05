from django.shortcuts import render, redirect,get_object_or_404
from .models import Profile
from django.contrib.auth.models import User
from . import forms
from django.contrib.auth import login, authenticate, logout, get_user_model,update_session_auth_hash 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

def profile_list(request):
    return render(request, 'profiles/list.html')

def profile_register(request):
    if request.method == "POST":
        form_user = forms.UserForm(request.POST)
        form_profile = forms.ProfileForm(request.POST, request.FILES)
        if form_user.is_valid() and form_profile.is_valid():
            email = form_user.cleaned_data['email']
            username = form_user.cleaned_data['username']
            # Check if username exists
            if User.objects.filter(username=username).exists():
                form_user.add_error('username', "This username is already taken.")
            # Check if email exists
            if User.objects.filter(email=email).exists():
                form_user.add_error('email', "This email is already in use.")
            # If there are errors, re-render the form with errors
            if form_user.errors:
                return render(request, 'profiles/register.html', {'form_user': form_user, 'form_profile': form_profile})

            # Save the user and profile
            user = form_user.save(commit=False)
            user.set_password(form_user.cleaned_data['password'])
            user.save()
            # Assuming you have signals for profile creation
            username = form_user.cleaned_data.get('username')
            password = form_user.cleaned_data.get('password')
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user:
                login(request, authenticated_user)
                messages.success(request, f'Account created for {username}!')
                return redirect('home')
            else:
                messages.warning(request, 'Authentication failed. Please try logging in.')
                return redirect('profile-register')
        else:
            # Form is invalid, re-render with errors
            return render(request, 'profiles/register.html', {'form_user': form_user, 'form_profile': form_profile})
    else:
        form_user = forms.UserForm()
        form_profile = forms.ProfileForm()
    return render(request, 'profiles/register.html', {'form_user': form_user, 'form_profile': form_profile})

def profile_login(request):
    if request.method == "POST":
        form_user = forms.LoginForm(request.POST)
        if form_user.is_valid():
            username = form_user.cleaned_data.get('username')
            print(username)
            password = form_user.cleaned_data.get('password')
            authenticated_user = authenticate(request, username = username,password = password)
            print(username, password)
            if authenticated_user:
                print('authenticated')
                login(request, authenticated_user)
                print('loffed in')
                messages.success(request, 'You have loggged in')
                return redirect('profile-list')
            else:
                messages.warning(request, 'Please Provide matching credentials')
        else:
            print('Form is invalid')
            messages.warning(request, 'Form is invalid')
    form_user = forms.LoginForm()
    context = {'form_user':form_user}
    return render(request, 'profiles/login.html', context)

@login_required
def profile_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')  # or any other page you want to redirect to

@login_required
def profile_update(request):
    user = request.user
    if request.method == 'POST':
        user_form = forms.UserUpdateForm(request.POST, instance=request.user)
        profile_form = forms.ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile-page', request.user.username) # Redirect to the same page or a success page
    else:
        user_form = forms.UserUpdateForm(instance=request.user)
        profile_form = forms.ProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profiles/update.html', context)

@login_required
def profile_password_update(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevents logout after password change
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('home')  # Redirect instead of rendering index.html
        else:
            messages.error(request, 'Error: Please check your input.')
            print(form.errors)  # Add this to debug errors

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profiles/password.html', {'form': form})

@login_required
def profile_page(request, username):
    user = get_object_or_404(User, username = username)
    is_own = False
    if request.user == user:
        is_own = True
    return render(request, 'profiles/profile.html', context = {'user':user, 'is_own':is_own})
