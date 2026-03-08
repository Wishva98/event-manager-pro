from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ORGANIZER = 'organizer'
    ATTENDEE = 'attendee'

    ROLE_CHOICES = [
        (ORGANIZER, 'Organizer'),
        (ATTENDEE, 'Attendee'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ATTENDEE)
    def __str__(self):
        return f"{self.username} ({self.role})"