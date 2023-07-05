from django import forms
from .models import File
# from .models import File,Folder

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
  
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file','is_private')
                  
# class DocumentForm(forms.ModelForm):
#     file = MultipleFileField()
#     class Meta:
#         model = File
#         fields = ('file', )


# class FolderForm(forms.ModelForm):
#     name=forms.CharField(max_length=100)
#     class Meta:
#         model = Folder
#         fields = ['name']


# class FolderUploadForm(forms.ModelForm):
#     # file = forms.FileField(widget=forms.MultipleFileInput(attrs={'multiple': True, 'webkitdirectory': True, 'directory': True}))
#     file = MultipleFileField(widget=forms.ClearableFileInput(attrs={'webkitdirectory': True, 'directory': True}))
#     class Meta:
#         model = Folder
#         fields = ['file',]
