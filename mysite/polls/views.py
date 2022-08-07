from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question
from .forms import QuestionForm


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return


def vote(request, question_id):
    return


def question_form(request):
    submitted = False
    if request.POST == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form?submitted=True')
    else:
        form = QuestionForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'polls/form.html', {'form': form, 'submitted': submitted})
