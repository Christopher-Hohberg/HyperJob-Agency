from django.db import models
import django.contrib.auth.models as mo


# Create your models here.
class Resume(models.Model):

    class Meta:
        app_label = "resume"

    description = models.TextField(max_length=1024)
    author = models.ForeignKey(mo.User, on_delete=models.CASCADE)

    r = models.Manager()


class Vacancy(models.Model):
    class Meta:
        app_label = "vacancy"

    description = models.TextField(max_length=1024)
    author = models.ForeignKey(mo.User, on_delete=models.CASCADE)

    r = models.Manager()


def get_vacancies():
    return Vacancy.r.all()


def get_resumes():
    return Resume.r.all()
