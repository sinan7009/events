import calendar

from django.shortcuts import render
from  calendar import HTMLCalendar
from datetime import datetime
from .models import Events
from .forms import VenueForm
from  django.http import HttpResponseRedirect


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_venue?submitted=True')

    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'events/add_venue.html',
                      {'form':form, 'submitted':submitted})


def all_events(request):
    event_list = Events.objects.all()
    return render(request, 'events/event_list.html',
                  {"event_list":event_list})
def home(request, year=datetime.now().year , month= datetime.now().strftime('%B')):
    name = "Sinan"
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)

    now =datetime.now()
    current_year = now.year

    time = now.strftime('%I:%M:%p')

    return render(request, 'events/home.html',{
        'name': name,
        'year': year,
        'month': month,
        "month_number" : month_number,
        'cal': cal,
        "current_year":current_year,
        "time": time,
    })
