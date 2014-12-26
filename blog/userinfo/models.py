from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SEX = (('male', 'male'), ('female', 'female'),)
OAUTH_SERVER = (
    ('tencent', 'qq'),
    ('sina', 'weibo'),
    ('baidu', 'baidu'),
)
class Userinfo(models.Model):
    #userid = models.CharField(max_length=128, primary_key=True, blank=False, unique=True)
    #password = models.CharField(max_length=256, blank=False)
    user = models.OneToOneField(User, primary_key=True)
    nikename = models.CharField(max_length=256, default='')
    avatar = models.CharField(max_length=256, default='')
    email = models.EmailField()
    sex = models.CharField(max_length=64, choices=SEX)
    authserver = models.CharField(max_length=128, choices=OAUTH_SERVER)
    token = models.TextField()

