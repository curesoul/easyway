from django.shortcuts import render

from .models import Detail, Lot, Item, Operator, Customer


def index(request):
    logs = Detail.objects.order_by('-batch')
    context = {
        'logs': logs
    }
    return render(request, 'mixs/index.html', context)


# def lot_list(request):
#     lots = Detail.objects.filter(lot__lot='220817', item__name='P6011NC')
#     context = {
#         "lots": lots,
#     }
#     return render(request, 'mixs/detail.html', context)


def lot_list(request):
    lots = Lot.objects.all()[0:30]
    details = Detail.objects.filter(lot__lot=[lots])
    context = {
        'lots': lots,
        'detail': details,
    }
    return render(request, 'mixs/lot_list.html', context)

