from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import About

# Create your views here.
def about(request):
    about = About.objects.get(pk=1)
    #_t = about.objects.filter(id=about_id).order_by('template').values('template').first()
    #template = _t['detail_blog.html']
    return render(request, 'about.html', {'about': about})
