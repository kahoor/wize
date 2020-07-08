from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Info(models.Model):
    ROLES_CHOICES = (
        ('EE', 'Employee'),
        ('EO', 'Employee of an organization'),
        ('DO', 'Director of an organization'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=ROLES_CHOICES, default='EE')
    organization = models.ForeignKey("organization.Organization", on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("account:userinfodetail", kwargs={"pk": self.pk})

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
