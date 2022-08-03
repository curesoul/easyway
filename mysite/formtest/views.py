from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import NameForm


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse('formtest:get_name'))
    else:
        form = NameForm()
    return render(request, 'formtest/index.html', {'form': form})
