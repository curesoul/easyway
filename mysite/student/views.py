from django.shortcuts import render

from .models import Student


def index(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'student/index.html', context)
