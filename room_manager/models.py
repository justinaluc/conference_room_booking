from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class ConferenceRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField(validators=[MinValueValidator(10),])
    projector = models.BooleanField(default=False)