from django.db import models

class Upload(models.Model):

    public = models.BooleanField()
    timestamp = models.TimeField(auto_now=True)
    file = models.FileField()

    def create(cls, public, file):
        upload = cls(
            public = public,
            file = file
        )
        return upload