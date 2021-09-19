from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new user
        """
        if not email:
            raise ValueError("Users must have an email address!")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Create and saves a new superuser
        """
        user =self.create_user(email, password)
        user.is_staff =True 
        user.is_superuser =True 
        user.save(using=self._db)

        return user   

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that supports email instead 
    of username
    """
    email       = models.EmailField(max_length=255, unique=True)
    name        = models.CharField(max_length=255, null=True)
    dateOfBirth = models.DateField(auto_now_add=False, auto_now=False, null=True)
    height      = models.FloatField(null=True)
    weight      = models.FloatField(null=True)
    phone_no    = models.BigIntegerField(null=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email' 


class UserData(models.Model):
    user        = models.ForeignKey(User, related_name='user_info', on_delete=models.CASCADE)
    steps       = models.IntegerField(default=0)
    calories    = models.FloatField(default=0)
    points      = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user) 
    
