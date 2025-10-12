from datetime import date
from time import timezone
from django.db import models
from django.core.validators import MinLengthValidator
from django.forms import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator
from django.utils import timezone

name_validator = RegexValidator(
    regex = r'^[a-zA-Z\s]+$',
    message = "This field should only contain alphabetic characters and spaces."
)

# Create your models here.
class Conference(models.Model):
    conference_id = models.AutoField(primary_key = True, unique = True, editable = False)
    name = models.CharField(max_length = 100, validators = [name_validator])
    Theme = [
        ('CS&AI', 'Computer Science & Artificial Intelligence'),
        ('SE', 'Science & Engineering'),
        ('SS&ED', 'Social Sciences & Education'),
        ('IT', 'Interdisciplinary Themes'),
    ]
    theme = models.CharField(max_length = 100, choices = Theme)
    location = models.CharField(max_length = 100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(validators = [
        MinLengthValidator(30, "Description must be at least 30 characters long.")
    ])
    created_at = models.DateTimeField(auto_now_add = True) # when the object is created
    updated_at = models.DateTimeField(auto_now = True) # when the object is updated
    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date.")

    def __str__(self):
        return  f"{self.name} + {self.theme} ({self.start_date} to {self.end_date})"

def generate_submission_id(self):
        return "SUB" + str(self.submission_id).zfill(8) # Generates a unique ID like SUB00000001

class Submission(models.Model):
    submission_id = models.AutoField(primary_key = True, unique = True, editable = False)
    user = models.ForeignKey('UserApp.User', on_delete = models.CASCADE, related_name = 'submissions')
    conference = models.ForeignKey(Conference, on_delete = models.CASCADE, related_name = 'submissions')
    title = models.CharField(max_length = 100)
    abstract = models.TextField()
    keywords = models.TextField()
    paper= models.FileField(
        upload_to = 'papers/',
        validators = [FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    Status = [
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    submission_date = models.DateField(auto_now_add = True)
    status = models.CharField(max_length = 100, choices = Status, default = 'submitted')
    payed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True) # when the object is created
    updated_at = models.DateTimeField(auto_now = True) # when the object is updated

    def validate_keywords(value):
        keywords = [keyword.strip() for keyword in value.split(',')]
        if len(keywords) > 10:
            raise ValidationError("You can only provide up to 10 keywords.")
        
    def clean(self):
        if self.conference.start_date < timezone.now().date():
            raise ValidationError("Submission date cannot be after conference start date.")
        # Limiter le nombre de soumissions par jour
        submissions_today = Submission.objects.filter(
            user=self.user,
            submission_date=timezone.now().date()
        ).count()
        if submissions_today >= 3:
            raise ValidationError("You can only submit 3 papers per day.")
        
    def save(self, *args, **kwargs):
        if not self.submission_id:
            new_submission_id = generate_submission_id(self)
            while Submission.objects.filter(submission_id=new_submission_id).exists():
                new_submission_id = generate_submission_id(self)
            self.submission_id = new_submission_id
        super().save(*args, **kwargs)

    
    


    


