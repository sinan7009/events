import calendar

from django.shortcuts import render
from  calendar import HTMLCalendar
from datetime import datetime
from .models import Events

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
