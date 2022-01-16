from django.shortcuts import render
from main import models ,forms
from django.views.generic import ( ListView ,DetailView , FormView)
from django.views.generic.detail import SingleObjectMixin

from django.http import HttpResponseRedirect
#these are overrides some function it doesnt handle views 


#  Create your views here.

class Index(ListView):
 model = models.Question 
 template_name = 'main/index.html'
 context_object_name = 'questions'


class Details(SingleObjectMixin ,  FormView):
    model = models.Question
    template_name = 'main/questions.html'
    form_class = forms.AnswerForm  


    def form_valid(self , form):
        obj = form.save(commit = False)
        obj.question  = self.get_object()
        obj.user = self.request.user 
        obj.save()
        return HttpResponseRedirect('/main')

    def get_context_data(self, **kwargs) :
        data = super().get_context_data(**kwargs) #it is dictionary
        data['answer'] = models.Answer.objects.get(
            question = self.get_object(),
            user = self.request.user 
        )
        return data 


 
    def post(self, request, *args, **kwargs) :
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        return self.render_to_response(context)
        



