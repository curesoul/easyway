from django.shortcuts import render, get_object_or_404

from myapp.models import Flower


def index(request):
    q = request.GET.get('q', None)
    items = ''
    if q is None or q is "":
        flowers = Flower.objects.all()
    elif q is not None:
        flowers = Flower.objects.filter(title__contains=q)
    context = {'flowers': flowers}
    return render(request, 'myapp/index.html', context)


def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'myapp/detail.html', {'flower': flower})


def tags(request, slug=None):
    flowers = Flower.objects.filter(tags__slug=slug)
    return render(request, 'myapp/index.html', {'flowers': flowers})
