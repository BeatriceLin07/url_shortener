from django.db import models

# Create your models here
class URL(models.Model):
    long_url = models.URLField(max_length=2048)
    short_code = models.CharField(max_length=10, unique=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.short_code} -> {self.long_url}"
