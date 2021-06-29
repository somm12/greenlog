from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def post(request):
    return render(request, 'post.html')

<<<<<<< HEAD
def each(request):
    return render(request, 'eachView.html')
=======
def normal_view_page(request):
    return render(request,'normal_view_page.html')

def plogging_view_page(request):
    return render(request, 'plogging_view_page.html')
>>>>>>> 033aa39ff0c467f9d84cf4b03aaecc1fc1d82a96
