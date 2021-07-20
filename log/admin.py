from django.contrib import admin
from .models import Post,User#,Plogging,Comment


admin.site.register(User)
admin.site.register(Post)
# admin.site.register(Plogging)
# admin.site.register(Comment)