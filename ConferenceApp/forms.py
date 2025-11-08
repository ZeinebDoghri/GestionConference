from django import forms
from .models import Conference, Submission


class ConferenceModel(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['name', 'start_date', 'end_date', 'location', 'theme', 'description']
        labels = {
            'name': 'Conference Name',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'location': 'Location',
            'theme': 'Theme',
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter conference name'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter location'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter description'}),
        }

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['conference', 'title', 'abstract', 'keywords', 'paper', 'status', 'payed']

        labels = {
            'conference': 'Select Conference',
            'title': 'Submission Title',
            'abstract': 'Abstract',
            'keywords': 'Keywords',
            'paper': 'Upload Paper (PDF)',
            'status': 'Submission Status',
            'payed': 'Payment Status',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter submission title'}),
            'abstract': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter abstract'}),
            'keywords': forms.TextInput(attrs={'placeholder': 'Enter keywords separated by commas'}),
            'status': forms.Select(),
            'payed': forms.CheckboxInput(),
        }
