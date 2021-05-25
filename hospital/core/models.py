from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()


class discharge(models.Model):
    today = models.IntegerField()
    total = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total = self.today + self.total
        super().save(*args, **kwargs)


class death(models.Model):
    today = models.IntegerField()
    total = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)


class normal_bed(models.Model):
    capacity = models.IntegerField()
    occupied = models.IntegerField()
    available = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)


class icu_bed(models.Model):
    capacity = models.IntegerField()
    occupied = models.IntegerField()
    available = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)


class ventilators(models.Model):
    capacity = models.IntegerField()
    occupied = models.IntegerField()
    available = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)


class OxygenCylinders(models.Model):
    capacity = models.IntegerField()
    occupied = models.IntegerField()
    available = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)


class HduBeds(models.Model):
    capacity = models.IntegerField()
    occupied = models.IntegerField()
    available = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)


class focalperson(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=250)
    email = models.EmailField()


# Create your models here.
class hospitals(models.Model):
    hospital_choice = (
        ("Government", "Government"),
        ("Private", "Private")
    )
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    hospital_type = models.CharField(max_length=10, choices=hospital_choice, default="Government")
    phone_no = models.CharField(max_length=125)
    images = models.ImageField(upload_to='images')
    lat = models.DecimalField(decimal_places=8, max_digits=10)
    long = models.DecimalField(decimal_places=8, max_digits=10)
    icu = models.OneToOneField(icu_bed, on_delete=models.CASCADE)
    normal = models.OneToOneField(normal_bed, on_delete=models.CASCADE)
    ventilators = models.OneToOneField(ventilators, on_delete=models.CASCADE)
    oxygen_plant = models.OneToOneField(OxygenCylinders, on_delete=models.CASCADE)
    discharge = models.OneToOneField(discharge, on_delete=models.CASCADE)
    death = models.OneToOneField(death, on_delete=models.CASCADE)
    hdu = models.OneToOneField(HduBeds, on_delete=models.CASCADE)
    focalperson = models.OneToOneField(focalperson, on_delete=models.CASCADE)
    user = models.ForeignKey(user, null=True, on_delete=models.CASCADE )

    def __str__(self):
        return self.name
