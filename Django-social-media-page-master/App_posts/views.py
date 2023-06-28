from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post,Like
from App_login.models import Follow
from django.contrib.auth.models import User


# Create your views here.
@login_required
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts=Post.objects.filter(author__in=following_list.values_list('following'))
    liked_post=Like.objects.filter(user=request.user)
    liked_post_list=liked_post.values_list('post',flat=True)
   # print(liked_post_list)
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains=search)
    return render(request, 'App_posts/home.html',
                  context={'title': 'home page', 'search': search, 'result': result,'posts':posts,})

@login_required
def liked(request,pk):
    post=Post.objects.get(pk=pk,user=request.user)
    already_liked=Like.objects.filter(post=post,user=request.user)
    if not already_liked:
        liked_post=Like(post=post,user=request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse('home'))

@login_required
def unlike(request,pk):
    post=Post.objects.get(pk=pk,user=request.user)
    already_liked=Like.objects.filter(post=post,user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))
