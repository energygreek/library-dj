import json
from bookmanage.models import BookInfo, BorrowDetail
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, JsonResponse
from django.urls.base import reverse
from django.utils import timezone
from polls.models import Choice, Question
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from django.core import serializers

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'bookmanage/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return BookInfo.objects.order_by('-book_id')[:5]

class DetailView(generic.DetailView):
    model = BookInfo
    template_name = 'bookmanage/detail.html'

def GetRentBook(request, name):
    #question = get_object_or_404(BorrowDetail, reader_id=name)
    json_result = serializers.serialize("json", BookInfo.objects.order_by('-book_id')[:5])
    fileds = json.loads(json_result)[0]['fields']
    return JsonResponse(fileds, safe=False)

def SearchBook(request):
    #question = get_object_or_404(BorrowDetail, reader_id=name)
    json_result = serializers.serialize("json", BookInfo.objects.order_by('-book_id')[:5])
    return JsonResponse(json_result, safe=False)

def OperateBook(request):
    #question = get_object_or_404(BorrowDetail, reader_id=name)
    json_result = serializers.serialize("json", BookInfo.objects.order_by('-book_id')[:5])
    return JsonResponse(json_result, safe=False)