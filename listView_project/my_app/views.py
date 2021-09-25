from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView, DeleteView)
from my_app import models
from django.urls import reverse_lazy
# Create your views here.

class indexView(TemplateView):
    template_name ='my_app/index.html'


class SchoolListView(ListView):
    #  we can create our own key of dictionary like
    context_object_name = 'schools'
    model = models.School
    # ListView return school_list   // modelName_list all in lower case
    
    
      
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School

    # we only provide template name for DetailView from CURD
    template_name ='my_app/school_details.html'

    # detailView return modelName    here school (all in lower case )


class SchoolCreateView(CreateView):
    # fields ='__all__'    but for security perpose we don't use fields then we include like
    # fields =('name','principal') we have 3 field in school
    # fields you want to create
    fields=('name','principal','location') 
    model = models.School

    # my_app/school_form.html <==== created by CreateView defalut ....school_form.html templates this automatically call school_form,html
    #  and also pass pk 


class SchoolUpdateView(UpdateView):
    # what can be updated school name can change ,principal can change  but location cann't be change
    # what field do you want to update 
    fields =('name','principal')
    model =models.School

class SchoolDeleteView(DeleteView):
    # default context_object_name = 'school ' or lower case version of model
    model =models.School

    # success_url attribute comes from django.urls
    # we use this because we donn't want to delete drunig runserver py file execute 
    # we want to delete afte success
    success_url =reverse_lazy('base_app:list') 

    # it calls school_confirm_delete.html so we form that one 




#  done by me
class StudentCreateView(CreateView):
    fields ='__all__'
    model =models.student
    # calls my_app/student_form.html