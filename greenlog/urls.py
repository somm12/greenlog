"""greenlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from log.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('login/',login, name="login"),
    path('signup/',signup, name="signup"),
    path('post/',post,name="post"),
<<<<<<< HEAD
    path('each/',each,name="each"),
=======
    path('normal_view_page/',normal_view_page, name="normal_view_page"),
    path('plogging_view_page/',plogging_view_page, name="plogging_view_page"),
>>>>>>> 033aa39ff0c467f9d84cf4b03aaecc1fc1d82a96
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)