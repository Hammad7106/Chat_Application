from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    groups = models.ManyToManyField('Group', blank=True)

    def __str__(self):
        return self.user.username



class Chat(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    content=models.CharField(max_length=1000)
    timestamp=models.DateTimeField(auto_now=True)
    group=models.ForeignKey('Group',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.user.username} in {self.group.name} - {self.timestamp}"

class Group(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name


