from django.contrib import admin
from .models import Blog, User, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Comment)
