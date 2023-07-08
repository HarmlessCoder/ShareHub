from django.urls import path
from .views import (PostCreateView,download_file,FileDelete,create_folder,
                    MyFileFolderView,home,download_folder,FolderDelete, 
                    toggle_favorite, FolderUpload, FolderUploadIndex)
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns =[
    path('', views.landing_page,name='landing_page'),
    path('home/',home ,name='home'),
    path('my_files/',MyFileFolderView.as_view(),name='all_files'),
    path('my_files/new/',PostCreateView.as_view(template_name='root/add_file.html'),name='all_files_create'),
    path('my_files/<int:pk>/delete/', FileDelete.as_view(), name='delete_file'),
    path('my_files/folder/create', create_folder,name='create_folder'),
    path('my_files/folder/create/<int:parent_folder_id>/',PostCreateView.as_view(template_name='root/add_file.html'),name='create_file_in_folder'),
    path('my_files/folder/create/folder/<int:parent_folder_id>/',create_folder,name='create_folder_in_folder'),
    path('my_files/<int:parent_folder_id>/',MyFileFolderView.as_view(template_name='root/subfolder.html'),name='subfolder'),
    path('download/file/<str:file_path>/', download_file, name='download_file'),
    path('download/folder/<int:pk>/', download_folder, name='download_folder'),
    path('delete/folder/<int:pk>/', FolderDelete.as_view(), name='delete_folder'),
    path('toggle_favorite/<str:model>/<int:pk>/', toggle_favorite , name='toggle_favorite'),
    path('folder_upload/<int:pk>/', FolderUpload, name='folder_upload'),
    path('folder_upload_index/', FolderUploadIndex, name='folder-upload-index'),
    path('preview/<int:file_id>/', views.preview_file, name='file_preview'),
    path('make_private/<int:file_id>/', views.make_private, name='make_private'),
    path('make_public/<int:file_id>/', views.make_public, name='make_public'),
    path('make_folder_private/<int:folder_id>/', views.make_folder_private, name='make_folder_private'),
    path('make_folder_public/<int:folder_id>/', views.make_folder_public, name='make_folder_public'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
