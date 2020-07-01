from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class UpgradeRequest(models.Model):
    STATUS_CHOICES = (
        ('ACC', 'Accepted'),
        ('REJ', 'Rejected'),
        ('WL', 'Waiting List'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_role = models.CharField(max_length=2)
    dream_role = models.CharField(max_length=2)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='WL')