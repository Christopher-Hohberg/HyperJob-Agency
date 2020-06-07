from django.db import models
import django.contrib.auth.models


# Create your models here.
class Vacancy(models.Model):

    class Meta:
        app_label = "vacancy"

    description = models.TextField(max_length=1024)
    author = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)


class Resume(models.Model):

    class Meta:
        app_label = "resume"

    description = models.TextField(max_length=1024)
    author = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)
