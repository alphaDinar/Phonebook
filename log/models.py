from django.db import models
from django.utils import timezone

class SuperMc(models.Model):
  username = models.CharField(max_length=300)
  phone = models.CharField(max_length=20)
  key = models.CharField(max_length=300)
  login_email = models.EmailField()
  login_password = models.CharField(max_length=300)
  timestamp = models.DateTimeField(default= timezone.now)
  class Meta:
    verbose_name_plural = 'Super Mc'

  def __str__(self):
    return f'{self.phone}'