from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import uuid


# Create your models here.

def generate_user_id():
    return "USER" + uuid.uuid4().hex[:4].upper() # Generates a unique ID like USER1A2B


def verify_email(email):
    domaine = ["esprit.tn", "gmail.com", "sesame.com", "central.com", "tek.tn"]
    email_domain = email.split('@')[1]
    if email_domain not in domaine:
        raise ValidationError("Email domain is not allowed.")
    
name_validator = RegexValidator(
    regex = r'^[a-zA-Z\s]+$',
    message = "This field should only contain alphabetic characters and spaces."
)
    


class User(AbstractUser):
    user_id = models.CharField(max_length = 8, primary_key = True, unique = True, editable = False)
    first_name = models.CharField(max_length = 100, validators = [name_validator])
    last_name = models.CharField(max_length = 100, validators = [name_validator])
    affiliation = models.CharField(max_length = 100)
    Role = [
        ('participant', 'Participant'),
        ('organisator', 'Organisator'),
        ('comite_member', 'Member of the Scientific Committee'),
    ]
    role = models.CharField(max_length = 100, choices = Role, default = 'participant')
    nationality = models.CharField(max_length = 100)
    email = models.EmailField(unique = True, validators = [verify_email])   
    created_at = models.DateTimeField(auto_now_add = True) # when the object is created
    updated_at = models.DateTimeField(auto_now = True) # when the object is updated
    #submissions = models.ManyToManyField('ConferenceApp.Conference', through='Submission') delete related_name in Submission model to use it this way
    #organizingCommitteesList = models.ManyToManyField('ConferenceApp.Conference', through='organizingCommittee') delete related_name in organizingCommittee model to use it this way

    # save method to generate user_id before saving the object
    def save(self,*args, **kwargs): #*args:  and **kwargs to pass any number of arguments
        if not self.user_id:
            new_user_id = generate_user_id()
            while User.objects.filter(user_id = new_user_id).exists(): # check if the generated user_id already exists
                new_user_id = generate_user_id()
            self.user_id = new_user_id
        super().save(*args, **kwargs) # call the real save() method
        



class organizingCommittee(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'committees')#use related_name to access all committees of a user
    conference = models.ForeignKey('ConferenceApp.Conference', on_delete = models.CASCADE, related_name = 'committees')#use related_name to access all committees of a conference
    Roles = [
        ('chair', 'Chair'),
        ('co-chair', 'Co-Chair'),
        ('member', 'Member'),
    ]
    committee_role = models.CharField(max_length = 100, choices = Roles)
    date_joined = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True) # when the object is created
    updated_at = models.DateTimeField(auto_now = True) # when the object is updated
   
