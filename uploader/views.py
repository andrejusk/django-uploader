from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .models import Upload
from .forms import UploadFileForm
import datetime


class Home(ListView):
    
    model = Upload
    context_object_name = 'uploads'
    template_name = 'home.html'

class Upload(FormView):

    form_class = UploadFileForm
    template_name = 'upload.html'
    success_url = '..'

    def post(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # user id doesn't properly get set
            instance = form.save(commit=False)
            instance.user = request.user
            instance.time = datetime.datetime.now()
            instance.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)