from django.contrib import admin
from .models import Venue
from .models import MyclubUser
from .models import Events

# admin.site.register(Venue)
admin.site.register(MyclubUser)
# admin.site.register(Events)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager',)
    list_display = ('name','event_date', 'venue')
    list_filter = ('event_date','venue')
    ordering = ('-event_date',)
