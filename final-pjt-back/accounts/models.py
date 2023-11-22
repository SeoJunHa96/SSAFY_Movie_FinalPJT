from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms import BooleanField
from rest_framework.authtoken.models import Token

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, nickname, password=None):
        if not username:
            raise ValueError('아이디를 꼭 적어주세요')
        user = self.model(
            username=username,
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, nickname, password=None):
        user = self.create_user(
            username=username,
            password=password,
            nickname=nickname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField("아이디", max_length=50, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    nickname = models.CharField("닉네임", max_length=50)
    email = models.EmailField(unique=False, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = ['nickname'] 
    
    objects = UserManager()
    
    def __str__(self):
        return self.fullname
    
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    
    def save(self, *args, **kwargs):
    # 사용자 저장 시 토큰 생성
        super().save(*args, **kwargs)
        Token.objects.get_or_create(user=self)
    
    @property
    def is_staff(self):
        return self.is_admin