from django.forms import ModelForm
from .models import Upload

class UploadFileForm(ModelForm):
    class Meta:
        model = Upload
        fields = [ 'public', 'file' ]