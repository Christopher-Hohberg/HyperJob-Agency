from django.shortcuts import render
from django.views import View
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
                               },
                      )
