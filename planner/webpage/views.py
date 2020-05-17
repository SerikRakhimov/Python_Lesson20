#from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse
from meeting.models import Meeting
from meeting.models import Room
from datetime import datetime

def welcome(request):
#   return HttpResponse(f"Hello")
    meetings = Meeting.objects.all()
    num_of_meetings = meetings.count()
    rooms = Room.objects.all()
    num_of_rooms = rooms.count()
    return render(request, 'webpage/welcome.html', {"meetings": meetings, "num_of_meetings": num_of_meetings, "rooms": rooms, "num_of_rooms": num_of_rooms })

"""
def date(request):
    #date = datetime.utcnow()
    date = datetime.now()
    return HttpResponse(f"{date}")
"""


# Create your views here.
