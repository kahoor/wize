from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class Duty(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    usersinfo = models.ManyToManyField("accounts.Info")
    title = models.CharField(max_length=50)
    describtion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("duties:dutydetailapi", kwargs={"pk": self.pk})
