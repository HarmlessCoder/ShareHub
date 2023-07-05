from django.contrib import admin
from .models import Post,File
# from .models import File,Folder,fav
# Register your models here.

admin.site.register(Post)


admin.site.register(File)
# admin.site.register(Folder)
# admin.site.register(fav)