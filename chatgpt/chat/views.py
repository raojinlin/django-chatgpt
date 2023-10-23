from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.
def hello(request: HttpRequest):
    return render(request=request, template_name='index.html')
