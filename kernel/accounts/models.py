from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Info(models.Model):
    ROLES_CHOICES = (
        ('EE', 'Employee'),
        ('EO', 'Employee of an organization'),
        ('DO', 'Director of an organization'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=ROLES_CHOICES, default='EE')
    # TODO: define a foregin key to organizations
    organization = models.ForeignKey("organization.Organization", on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.user.username

    def make_DO(self, org):
        print('yes')
        self.role = 'DO'
        self.organization = org

    def make_EO(self, org):
        self.role = 'EO'
        self.organization = org

    def make_EE(self):
        self.role = 'EE'
        self.organization = None
