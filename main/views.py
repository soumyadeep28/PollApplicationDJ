from django.shortcuts import render
from main import models ,forms
from django.views.generic import ( ListView ,DetailView , FormView)
from django.views.generic.detail import BaseDetailView

from django.http import HttpResponseRedirect
#these are overrides some function it doesnt handle views 


#  Create your views here.

class Index(ListView):
 model = models.Question 
 template_name = 'main/index.html'
 context_object_name = 'questions'


class Details(BaseDetailView ,  FormView):
    model = models.Question
    template_name = 'main/questions.html'
    form_class = forms.AnswerForm  


    def form_valid(self , form):
        obj = form.save(commit = False)
        obj.user = self.request.user 
        obj.save()
        
        return HttpResponseRedirect('/')
        



