from django.shortcuts import render
from .models import Post, Contact
from django.http import HttpResponseRedirect

# Create your views here.


def starting_page(request):
    posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'home.html', {"posts": posts,"more":True})


def posts(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, 'home.html', {"posts": posts,"more":False})


def post_details(request,slug):
    post=Post.objects.get(slug=slug)
    print(post)
    return render(request,'blog.html',{'post':post})


def about(request):
    return render(request, 'profile.html')


def contact(request):
    return render(request, 'contact.html')


def submit(request):
    if request.method == 'POST':
        message = Contact(
            name=request.POST['name'], mail=request.POST['email'], message=request.POST['message'])
        message.save()
        return render(request, 'thanks.html')


def invalid(request,slug):
    return HttpResponseRedirect('/')
