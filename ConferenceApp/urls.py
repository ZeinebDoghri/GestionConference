from django.urls import path
#from . import views
from .views import *

urlpatterns = [
    #path('liste/', views.all_conferences, name='list_conferences'),
    path('liste/', ConferenceListView.as_view(), name='list_conferences'),
    path('detail/<int:pk>/', ConferenceDetailView.as_view(), name='conference_detail'),
]