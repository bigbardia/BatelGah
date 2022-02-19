import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.urls import reverse
from django.utils.text import slugify


class Token(models.Model):
    
    token = models.UUIDField(primary_key=False , default=uuid.uuid4,unique=True,editable=False)

    def get_absoloute_url(self):
        return reverse("verification" , kwargs={"pk":self.pk})


class UserManager(BaseUserManager):

    def create_user(self,email,password,username=None , is_admin = False , is_active = False , is_staff=False , token = None):
        if not email:
            raise ValueError("Users Must have email address!")
        if not password:
            raise ValueError("Users Must Have Password!")

        user = self.model(email=self.normalize_email(email))
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.token = token
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,password , username=None):
        user = self.create_user(email=email , password=password , is_active=True , is_admin=True , is_staff=True , username = username)
        return user


            

class User(AbstractBaseUser):
    #important fields
    email = models.EmailField(unique=True)
    slug = models.SlugField(max_length=20 , unique=True ,  blank=True)
    token = models.OneToOneField(Token , on_delete=models.CASCADE , null = True , blank=True)
    #profile fields
    date_joined = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=48 , blank=True)
    about = models.TextField(blank=True , null=True)
    status = models.CharField(max_length=50 , blank=True , null=True)
    #boring stuff
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects=  UserManager()

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    def get_absoloute_url(self):
        return reverse("profilesummary" , kwargs={"slug" : self.slug})


    def get_email_name(self):
        res= ""
        for c in self.email:
            if c == "@":
                break
            else:
                res += c
        return res


    def save(self,*args , **kwargs):        
        if self.username is None or self.username == "":
            self.username = self.get_email_name()
        super().save(*args , **kwargs)
        if not self.slug:
            self.slug = slugify(self.get_email_name()+str(self.pk))


        return super().save(*args , **kwargs)

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin

    def __str__(self):
        return self.email



