from django.conf import settings
from django.db import models
from django.utils import timezone


class Experiences(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True)
    work_title = models.CharField(max_length=150)
    start_end_dates = models.CharField(max_length=50)
    company = models.CharField(max_length=150)
    experience_desp = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.work_title
