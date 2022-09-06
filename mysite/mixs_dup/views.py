from django.shortcuts import render, get_object_or_404

from .models import Customer, Operator, Item, Lot, ProductionPlan, Detail, DetailChangeLog


def index(request):
    pps = ProductionPlan.objects.all()
    context = {
        'pps': pps,
    }
    return render(request, 'mixs_dup/index.html', context)


def detail(request, pp_id):
    detail = get_object_or_404(ProductionPlan, pk=pp_id)
    return render(request, 'mixs_dup/detail.html', {'detail': detail, })


def results_sheet(request, pp_id):
    detail = get_object_or_404(ProductionPlan, pk=pp_id)
    batch_start = request.POST.get('batch-start', None)
    batch_end = request.POST.get('batch-end', None)
    batch_control = '"' + batch_start + ':' + batch_end + '"'
    return render(request, 'mixs_dup/results_sheet.html',
                  {'detail': detail, 'batch_start': batch_start, 'batch_end': batch_end,
                   'batch_control': batch_control, })
