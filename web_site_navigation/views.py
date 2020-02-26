from web_site_manage.settings import CUSTOMIZE_OPTION
from django.shortcuts import render,HttpResponse,redirect
from web_site_navigation import models


# Create your views here.

def index(request):
    if request.method == 'GET':
        web_class = models.web_class.objects.all()
        web_class_obj = models.web_class_obj.objects.all()
        web_site = models.web_site.objects.all()



        return render(request, 'index.html',{
            'web_site_name':CUSTOMIZE_OPTION['web_site_name'],
            'web_class':web_class,
            'web_class_obj':web_class_obj,
            'web_site':web_site,
        })
