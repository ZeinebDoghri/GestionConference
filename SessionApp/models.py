from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

room_validator = RegexValidator(
    regex = r'^[a-zA-Z0-9\s]+$',
    message = "This field should only contain alphanumeric characters and spaces."
)

# Create your models here.
class Session(models.Model):
    session_id = models.AutoField(primary_key = True, unique = True, editable = False)
    title = models.CharField(max_length = 100)
    topic = models.CharField(max_length = 100)
    session_day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length = 100, validators = [room_validator])
    conference = models.ForeignKey('ConferenceApp.Conference', on_delete = models.CASCADE, related_name = 'sessions')# or import Conference from ConferenceApp.models
    created_at = models.DateTimeField(auto_now_add = True) # when the object is created
    updated_at = models.DateTimeField(auto_now = True) # when the object is updated
    # Validate that the session_day is within the conference dates and that end_time is after start_time
    def clean(self):
        if self.session_day < self.conference.start_date or self.session_day > self.conference.end_date:
            raise ValidationError("La date de la session doit être comprise dans l'intervalle de la conférence.")
        if self.end_time <= self.start_time:
            raise ValidationError("L'heure de fin doit être postérieure à l'heure de début.")
