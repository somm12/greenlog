from django.contrib import admin
from .models import Post,Plogging,User,Comment


admin.site.register(User)
admin.site.register(Post)
admin.site.register(Plogging)
admin.site.register(Comment)