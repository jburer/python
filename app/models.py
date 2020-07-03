from django.db import models
from django.utils import timezone

# Create your models here.
class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField(("date logged"), auto_now=False, auto_now_add=False)

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class AuthenticatorStorage(models.Model):
    store_date = models.DateTimeField(("date logged"), auto_now=False, auto_now_add=False)
    derived_secure_hash = models.CharField(max_length=300)

    def __str__(self):
        