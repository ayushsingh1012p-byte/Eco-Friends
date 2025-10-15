from django.shortcuts import render
from .models import Event
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def events_view(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events.html', {'events': events})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})
