
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User 
import hashlib
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Membre(models.Model):

    id = models.AutoField(primary_key=True)
    username= models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    code_invitation =  models.CharField(max_length=10)
    password = models.CharField(max_length=128)
    type = models.IntegerField()
    description = models.TextField(null=True)
    

    
    class Meta:
        db_table = 'membre'

    def __str__(self):
         return (self.email )


    def save(self, *args, **kwargs):
        # Hash the password before saving
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Invitation(models.Model):
    code = models.CharField(max_length=10)
    valeur = models.IntegerField()

    class Meta:
        db_table = 'invitation'
     

    def __str__(self):
        return self.code


class Workshop(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')

    class Meta:
        db_table='workshop'

    def __str__(self):
        return self.name


import hashlib
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Picture(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='galery/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_hash = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.title

@receiver(pre_save, sender=Picture)
def generate_image_hash(sender, instance, **kwargs):
    if instance.image:
        image_content = instance.image.read()
        image_hash = hashlib.md5(image_content).hexdigest()
        instance.image_hash = image_hash
