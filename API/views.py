from django.shortcuts import render
from django.views.generic import TemplateView
from .services import get_droplets

def GetDroplets(TemplateView):
    
    template_name = 'droplets.html'
    def get_context_data(self, *args, **kwargs):
        context = {'droplets': get_droplets(),}
        
        return context
    
    

            
    