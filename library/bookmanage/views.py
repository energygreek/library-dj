from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.utils import timezone
from polls.models import Choice, Question
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]