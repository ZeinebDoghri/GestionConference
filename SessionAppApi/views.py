from django.shortcuts import render
from rest_framework import viewsets
from SessionApp.models import Session
from .serializers import SessionSerializer

# Create your views here.
class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    filter_backends = viewsets.ModelViewSet.filter_backends
    filterset_fields = ['conference', 'conference_id', 'room', 'session_day', 'topic']
    search_fields = ['title', 'topic', 'room']
    ordering_fields = ['start_time', 'end_time', 'title']
    ordering = ['start_time']

    
