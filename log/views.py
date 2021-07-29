from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method== 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        nickname = request.POST.get('nickname', None)
        password = request.POST.get('password', None)
  
    res_data = {}
    if not (nickname and password):
        res_data['error'] = '모든 값을 입력해야 합니다.'
        return render(request, 'login.html', res_data)
        
    else:
        try: 
            user = User.objects.get(nickname = nickname)
            if check_password(password, user.password):
                request.session['user'] = user.nickname
                return redirect('home')
            else:
                res_data['error'] = '아이디와 비밀번호를 다시 확인해주세요.'
                return render(request, 'login.html', res_data)
        except: 
            res_data['error'] = '아이디와 비밀번호를 다시 확인해주세요.'
            return render(request, 'login.html', res_data)

    if user is not None:
        self.request.session['nickname'] = nickname
        login(self.request, user)
        remember_session = self.request.POST.get('remember_session', False)
        if remember_session:
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
    return redirect("home")

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
            nickname = request.POST['nickname']
            name = request.POST['name']
            password = request.POST['password']
            passwordcheck = request.POST['passwordcheck']

            res_data = {} #응답 메시지를 담을 변수(딕셔너리)
            try:
                print(0)
            except print(0):
                pass
            if not (password and passwordcheck and nickname and name):
                res_data['error'] = '모든 값을 입력해야 합니다.'
                return render(request, 'signup.html', res_data)
            elif password != passwordcheck:
                res_data['error'] = '비밀번호가 다릅니다'
                return render(request, 'signup.html', res_data)
            elif User.objects.filter(nickname = request.POST['nickname']).exists():
                res_data['error'] = '이미 존재하는 닉네임입니다.'
                return render(request, 'signup.html', res_data)
            else:
                user = User( # 모델에서 생성한 User 클래스를 가져와 객체 생성
                    nickname = nickname,
                    name = name,
                    password = make_password(password),
                )

                user.save() #데이터베이스에 저장
                return render(request, 'signup_done.html', {'message': '회원가입을 완료하였습니다.'})
    return render(request, 'signup.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('home.html')


def mypage(request):
    return render(request, 'mypage.html')


def each(request, post_id): 
    MyPost = get_object_or_404(Post, pk = post_id)
    Writer= User.objects.get(pk=MyPost.writer)
    like="false"
    if request.method == "POST":
        try:
            user=request.session['user']
            users_list=MyPost.like_users.all()
            for users in users_list:
                if(users.nickname == user):
                    MyPost.like_users.remove(user)
                    MyPost.like-=1
                    MyPost.save()
                    if (MyPost.kinds=="플로깅" ):
                        return render(request, 'eachPlogging.html',{'MyPost':MyPost,'Writer':Writer,'like':like})
                    else :
                        return render(request, 'eachNomal.html',{'MyPost':MyPost,'Writer':Writer,'like':like})
            like="true"
            MyPost.like_users.add(user)
            MyPost.like+=1
            MyPost.save()
        except:
            messages.warning(request, '로그인이 필요합니다.')
            return redirect('login')
    if (MyPost.kinds=="플로깅" ):
        return render(request, 'eachPlogging.html',{'MyPost':MyPost,'Writer':Writer,'like':like})
    else :
        return render(request, 'eachNomal.html',{'MyPost':MyPost,'Writer':Writer,'like':like})



def create(request):
    new_post = Post()
    new_post.kinds=request.POST['volunteerKinds']
    new_post.title=request.POST['title']
    new_post.writer=request.session['user']
    new_post.content=request.POST['contentInput']
    if request.FILES.get('images') :
        new_post.image=request.FILES.get('images')
    else :
        new_post.image= "../static/images/noPhoto.png"
    print(new_post.image)
    place1 = request.POST["h_area1"]
    place2 = request.POST["h_area2"]
    new_post.firstPlace=place1+'-'+place2
    new_post.like=0
    new_post.date= timezone.datetime.now()
    new_post.save()
    return redirect('home')

def post(request):
    return render(request, 'post.html')

def plogging(request):
    return render(request, 'plogging.html')

def container(request):
    return render(request, 'container.html')

def gogo(request):
    return render(request, 'gogo.html')

def vegetarian(request):
    posts=Post.objects.all().filter(kinds='채식')
    return render(request, 'vegetarian.html',{'posts':posts})

def others(request):
    return render(request,'others.html')

def yesUp(request,post_id):
    post = Post.objects.get(id=post_id)
    post.like+=1
    post.save()
    print(post.like)
    return render(request, 'eachPlogging.html')
   