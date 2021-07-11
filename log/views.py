from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def post(request):
    return render(request, 'post.html')


def mypage(request):
    myposts = Post.objects
    search = request.GET.get('search')
    if search == 'true':
        writer = request.GET.get('writer')
        myposts = Post.objects.filter(author = writer)
    return render(request, 'mypage.html',{'myposts':myposts})


def each(request):
    return render(request, 'eachView.html')

def others(request):
    return render(request,'others.html')

def plogging(request):
    return render(request, 'plogging.html')

def container(request):
    return render(request, 'container.html')

def gogo(request):
    return render(request, 'gogo.html')

def vegetarian(request):
    return render(request, 'vegetarian.html')

