from django.shortcuts import render, HttpResponseRedirect
from .forms import CreateNewUser, Edit_ProfileForm
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse, reverse_lazy
from .models import UserProfile, Follow
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from App_posts.forms import PostForm
from django.contrib.auth.models import User


# Create your views here.

def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            return HttpResponseRedirect(reverse('App_login:login'))

    return render(request, 'App_login/sign_up.html', context={'title': 'signup.Instagram', 'form': form})


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_posts:home'))
    return render(request, 'App_login/login.html', context={'title': 'login', 'form': form})


@login_required
def edit_profile(request):
    current_user = UserProfile(user=request.user)
    form = Edit_ProfileForm(instance=current_user)
    if request.method == 'POST':
        form = Edit_ProfileForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = Edit_ProfileForm(instance=current_user)
            return HttpResponseRedirect(reverse('App_login:profile'))
    return render(request, 'App_login/profile.html', context={'title': 'profile.social', 'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_login:login'))


@login_required
def Profile(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'App_login/user.html', context={'form': form})


@login_required
def user(request, username):
    user_other = User.objects.get(username=username)
    #already_followed = Follow.objects.filter(follower=request.user, following=request.user)
    if user_other == request.user:
        return HttpResponseRedirect(reverse('App_login:profile'))

    return render(request, 'App_login/user_others.html',
                  context={'user_other': user_other,})


@login_required
def follow(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    if not already_followed:
        followed_user=Follow(follower=follower_user, following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('App_login:user', kwargs={'username': username}))


@login_required
def unfollow(request, username):
    following_user= User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('App_login:user', kwargs={'username': username}))
