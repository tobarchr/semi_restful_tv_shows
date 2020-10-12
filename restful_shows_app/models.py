from django.db import models
from _datetime import date,datetime

class showsManager(models.Manager):
    def basic_validator(self, postData):
        time_changed = datetime.strptime(postData['release_date'],"%Y-%m-%d")
        now = datetime.now()
        errors={}
        if len(postData['title']) <2:
            errors['title'] = "Title name should be at least 2 characters"

        if len(postData['network']) <3:
            errors['network'] = "Network should be at least 3 characters"

        if len(postData ['desc'])<10 and len(postData ['desc'])>0:
            errors['desc'] = "Description should be at least 10 characters"

        if time_changed > now:
            errors['release_date'] = "Release date cannot be future date"

        return errors

class shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = showsManager()
    