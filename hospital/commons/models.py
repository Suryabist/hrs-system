from django.db import models


# Create your models here.
class Corona(models.Model):
    tested_sample = models.IntegerField()
    infected = models.IntegerField()
    recovered = models.IntegerField()
    death = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)


class contact(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    hospital = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name
