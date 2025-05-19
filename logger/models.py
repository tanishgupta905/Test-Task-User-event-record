from django.db import models
from django.contrib.auth.models import User


class UserActivity(models.Model):
    EVENT_TYPES = [
        ('page_view', 'Page View'),
        ('click', 'Click'),
        ('form_submit', 'Form Submit'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    timestamp = models.DateTimeField()
    metadata = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.event_type} at {self.timestamp}"
    
