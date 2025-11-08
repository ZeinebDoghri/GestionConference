from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import ConferenceModel, SubmissionForm
from .models import Conference, Submission
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

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

class ConferenceCreate(LoginRequiredMixin, CreateView):
    model = Conference
    template_name = 'Conference/conference_form.html'  # Specify your template name/location
    #fields = "__all__"
    form_class = ConferenceModel # Use the custom form
    success_url = reverse_lazy('list_conferences')  # Redirect to conference list after creation


class ConferenceUpdate(LoginRequiredMixin, UpdateView):
    model = Conference
    template_name = 'Conference/conference_form.html'  # Specify your template name/location
    #fields = "__all__"
    form_class = ConferenceModel
    success_url = reverse_lazy('list_conferences')  # Redirect to conference list after update

class ConferenceDelete(LoginRequiredMixin, DeleteView):
    model = Conference
    template_name = 'Conference/conference_confirm_delete.html'  # Specify your template name/location
    success_url = reverse_lazy('list_conferences')  # Redirect to conference list after deletion


class UserSubmissionListView(LoginRequiredMixin, ListView):
    model = Submission
    template_name = 'Conference/submission_list.html'
    context_object_name = 'list_submissions'

    def get_queryset(self):
        # the user can see only his submissions
        return Submission.objects.filter(user=self.request.user)

class DetailSubmissionView(LoginRequiredMixin, DetailView):
    model = Submission
    template_name = 'Conference/detail_submission.html'
    context_object_name = 'submission'

class AddSubmissionView(LoginRequiredMixin, CreateView):
    model = Submission
    template_name = 'Conference/submission_form.html'
    form_class = SubmissionForm
    success_url = reverse_lazy('list_submissions')

    def form_valid(self, form):
        form.instance.user = self.request.user   # attach user here
        return super().form_valid(form)
    
class UpdateSubmissionView(LoginRequiredMixin, UpdateView):
    model = Submission
    template_name = 'Conference/submission_form.html'
    form_class = SubmissionForm
    success_url = reverse_lazy('list_submissions')

    def dispatch(self, request, *args, **kwargs):
        submission = self.get_object()
        if submission.status in ['accepted', 'rejected']:  # accepted or rejected
            messages.error(request, "You cannot edit an accepted or rejected submission.")
            return redirect('list_submissions')  # or the page you want
        return super().dispatch(request, *args, **kwargs)

    





