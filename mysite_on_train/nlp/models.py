from django.db import models
from django.urls import reverse

# Create your models here.
class InputMessage(models.Model):
    text = models.TextField(null=False)
    client = models.CharField(max_length=30)
    upload_date = models.DateField()

    def get_absolute_url(self):
        return reverse('process_view',kwargs={'pk':self.id})

