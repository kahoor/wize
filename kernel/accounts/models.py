from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Info(models.Model):
    ROLES_CHOICES = (
        ('SA', 'Site Admin'),
        ('EE', 'Employee'),
        ('EO', 'Employee of an organization'),
        ('DO', 'Director of an organization'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=ROLES_CHOICES, default='EE')
    # TODO: define a foregin key to organizations

    def __str__(self):
        return self.user.username
