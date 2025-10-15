from django.urls import path
from .views import challenges_view, submit_challenge
urlpatterns = [
    path('', challenges_view , name='challenges'),
    path('submission/', submit_challenge, name='submission'),

]
