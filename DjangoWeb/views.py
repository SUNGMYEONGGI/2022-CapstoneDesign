from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student

def index(request):
    return render(request, 'DjangoWeb/index.html')

def createform(request):

    if request.method == 'POST':
        std = Student()
        std.studentID = request.POST['studentID']
        std.name = request.POST['name']
        std.major = request.POST['major']
        std.save()

    return redirect('home')