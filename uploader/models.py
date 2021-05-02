from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class Upload(models.Model):

    user = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
    )
    public = models.BooleanField()
    time = models.TimeField()
    file = models.FileField(
        upload_to='uploads/%Y/%m/%d/'
    )