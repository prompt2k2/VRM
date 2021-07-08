from django.shortcuts import render
from django.views.generic import TemplateView

def GetDataView(request):
    
    template_name = 'getdataview.html'
    return render(request, template_name)
    

            
    