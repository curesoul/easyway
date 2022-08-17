from django.shortcuts import render

from .models import Detail


def index(request):
    logs = Detail.objects.order_by('-batch')
    context = {
        'logs': logs
    }
    return render(request, 'mixs/index.html', context)


def lot_list(request):
    lots = Detail.objects.filter(lot__lot='220817', item__name='P6011NC')
    context = {
        "lots": lots,
    }
    return render(request, 'mixs/detail.html', context)
