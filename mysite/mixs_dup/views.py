from django.shortcuts import render

from .models import Customer, Operator, Item, Lot, ProductionPlan, Detail, DetailChangeLog


def index(request):
    pps = ProductionPlan.objects.all()
    context = {
        'pps': pps
    }
    return render(request, 'mixs_dup/index.html', context)

