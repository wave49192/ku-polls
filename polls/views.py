"""Views Page."""
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from .models import Question, Choice


class IndexView(generic.ListView):
    """Index View Class."""

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be published in the future).

        Returns: Last Five Questions
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """Detail View."""

    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    """Result View."""

    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    """Vote Function If no vote return to page before and print the message."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def detail(request, question_id=None):
    """Return poll not available or go to detail page."""
    question = get_object_or_404(Question, pk=question_id)
    if not question.can_vote():
        messages.error(request, f'{"Poll not available"}')
        return HttpResponseRedirect(reverse('polls:index'))
    else:
        return render(request, 'polls/detail.html', {'question': question, })
