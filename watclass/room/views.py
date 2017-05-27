from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template import loader

from openroom.models import Room, Lecture


def index(request):
    return HttpResponse('')

def detail(request, question_id):
    try:
        room = Room.objects.get(code=question_id)
        print(question_id)
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    return render(request, 'room/detail.html', {'room': room})

def lecture(request, question_id, lecture_id):
    try:
        room = Room.objects.get(code=question_id)
        lecture = room.lecture_set.get(id_num = lecture_id)
    except Room.DoesNotExist or Lecture.DoesNotExist:
        raise Http404("Lecture does not exist")
    return render(request, 'room/lecture.html', {'lecture': lecture})





