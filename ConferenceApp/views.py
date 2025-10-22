from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView, DetailView

# Create your views here.
#function to display all conferences using request
def all_conferences(request):
    conferences = Conference.objects.all()
    return render(request, 'Conference/list.html', {'list_conferences': conferences})

#class to display all conferences
class ConferenceListView(ListView):
    model = Conference
    template_name = 'Conference/list.html'  # Specify your template name/location
    context_object_name = 'list_conferences'
    ordering = ['-start_date']  # Order by start_date descending

class ConferenceDetailView(DetailView):
    model = Conference
    template_name = 'Conference/detail.html'  # Specify your template name/location
    context_object_name = 'conference'


