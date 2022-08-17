from django.shortcuts import render

from .models import Detail


def index(request):
    logs = Detail.objects.all()
    context = {
        'logs': logs
    }
    return render(request, 'mixs/index.html', context)
