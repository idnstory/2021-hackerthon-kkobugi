from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def hello(request):
    return HttpResponse("hello")

def camera(request):
    return render(request, "camera.html")
