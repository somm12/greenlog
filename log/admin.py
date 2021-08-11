from django.contrib import admin
from .models import Post,User,Photo



class PhotoInline(admin.TabularInline):
    model = Photo

class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]


admin.site.register(Post, PostAdmin)
admin.site.register(User)
