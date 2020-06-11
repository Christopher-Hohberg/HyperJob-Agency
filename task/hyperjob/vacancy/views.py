from django.shortcuts import render
from django.views import View
import resume.models


# Create your views here.
class VacancyView(View):
    def get(self, request, *args,**kwargs):
        return render(request,
                      "vacancy/vacancies.html",
                      context={
                          "vacancies_list": resume.models.get_vacancies(),
                            },
                      )
