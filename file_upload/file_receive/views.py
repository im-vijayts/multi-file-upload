from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *

def Form(request):
    return render(request, "file_receive/form.html", {})

def Upload(request):
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f):
            with open('./media/images/' + str(count) + '.jpg', 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x)
    return HttpResponse("File(s) uploaded!")

