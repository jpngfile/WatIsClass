from django.template import loader
from .models import Room



# noinspection PyPep8

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


import random, string

from .forms import RoomForm

from .forms import CourseForm, RoomForm



def index(request):
    template = loader.get_template('openroom/homepage.html')
    return HttpResponse(template.render(request))
@csrf_exempt

def search(request):
    query = request.GET['course']
    print(query)
    return HttpResponseRedirect("/room/" + query)




@csrf_exempt
def generate(request):
    # if this is a POST request we need to process the form data
    # noinspection PyPep8,PyPep8,PyPep8,PyPep8,PyPep8

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CourseForm(request.POST)
        # check whether it's valid:


        if form.is_valid():
            room_code = ''

            for x in range(0, 10):
                room_code += random.choice(string.ascii_letters)
            room = Room(lectures=form.cleaned_data['num_lectures'],name=form.cleaned_data['course'],code=room_code)

            room.code = room_code;

            room.save();
            return HttpResponse('You can visit your room at ' + room.code)

        # noinspection PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8
        if form.is_valid():
            room_code = ''
            # noinspection PyPep8,PyPep8
            for x in range(0, 10):
                room_code += random.choice(string.ascii_letters)
            room = Room(lectures=form.cleaned_data['num_lectures'],name=form.cleaned_data['course'],code=room_code)
            # noinspection PyPep8
            room.code = room_code;
            # noinspection PyPep8
            room.save();
            return HttpResponse('You can visit your room at ' + room_code)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = CourseForm()

    return render(request, 'openroom/index.html', {'form': form})
