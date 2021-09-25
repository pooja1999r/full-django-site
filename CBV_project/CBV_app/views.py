from typing import SupportsAbs
from django.shortcuts import render
from django.views.generic import View,TemplateView

# from django.http import HttpResponse



# Create your views here

"""
function based view
"""
# def index(request):
#     return render(request,'CBV_app/index.html')




"""
class based view
"""
# class index(View):
#     def get(self,request):                  # inbult function
#         return HttpResponse("hellow WoRld ")




# Template based class view
class index(TemplateView):
    template_name ='CBV_app/index.html'            #    template_name <=  class based generic object 

    
    # inject context diction into tempaltes
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context[' injectme '] = 'hey there i am using whatsapp'
            return context
        