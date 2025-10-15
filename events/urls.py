from django.urls import path
from .views import events_view, event_detail
urlpatterns = [
    path('', events_view, name='events'), 
    path('<int:event_id>/', event_detail, name='event_detail'),
]
