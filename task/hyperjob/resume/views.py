from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
import resume.models


menu_ = [
         {
             "link": "/login",
             "name": "login",
         },
         {
             "link": "/signup",
             "name": "signup",
         },
         {
             "link": "/vacancies",
             "name": "vacancies",
         },
         {
             "link": "/resume",
             "name": "resume",
         },
         {
             "link": "/home",
             "name": "home",
         },
        ]


# Create your views here.
class IndexView(View):
    def get(self, request, *args, ** kwargs):
        return render(request,
                      "index.html",
                      context={
                          "menu": menu_,
                               }
                      )


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request,
                      "resume/resume.html",
                      context={
                          "resume_list": resume.models.get_resumes(),
                               }
                      )


class MyProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request,
                      "home.html",
                      context={

                               }
                      )


class CreateNew(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff and "vacancy" in request.path:
                b = resume.models.Vacancy(author=request.user,
                                          description=request.POST.get("description"))
                b.save()
            elif not request.user.is_staff and "resume" in request.path:
                b = resume.models.Resume(author=request.user,
                                         description=request.POST.get("description"))
                b.save()
            else:
                raise PermissionDenied
            return render(request,
                          "home.html",
                          context={

                                   }
                          )
        else:
            raise PermissionDenied


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    success_url = "home"
    template_name = "login.html"


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = "login"
    template_name = "signup.html"
