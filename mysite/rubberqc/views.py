from django.shortcuts import render, HttpResponseRedirect

from .forms import MixSForm


def index(request):
    if request.method == 'POST':
        form = MixSForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            form = MixSForm()
        return render(request, 'rubberqc/index.html', {'form': form})
