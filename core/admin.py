from django.contrib import admin
from .models import Post, Category
# Register your models here.
# You need to register your models to show up in django admin panel.
# For accessing admin panel you need to create a superuser. For that write command py manage.py createsuperuser 
admin.site.register(Post)
admin.site.register(Category)