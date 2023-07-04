from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import views as auth_views
from PIL import Image

# Create your models here.

class profile(models.Model):
    # profilename = models.CharField(max_length=100)
    # DOB = models.DateField()
    # college = models.CharField(max_length=100)
    # created = models.DateTimeField(default=timezone.now)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to = 'profile_pic')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


# class profile(models.Model):
#     profilename = models.CharField(max_length=100)
#     DOB = models.DateField()
#     college = models.CharField(max_length=100)
#     created = models.DateTimeField(default=timezone.now)
#     image = models.ImageField(upload_to='profilepic')
#     owner=models.OneToOneField(User,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.profilename