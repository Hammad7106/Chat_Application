from django.contrib import admin
from .models import UserProfile,Chat,Group
# Register your models here.

@admin.register(UserProfile)
class User(admin.ModelAdmin):
    list_display = ('user','image')

@admin.register(Chat)
class User_Chat(admin.ModelAdmin):
    list_display = ('user','content','timestamp','group')


@admin.register(Group)
class User_Chat(admin.ModelAdmin):
    list_display = ('id','name')
