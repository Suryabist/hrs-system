from django.db import models


class location(models.Model):
    lat = models.DecimalField(decimal_places=5, max_digits=10)
    long = models.DecimalField(decimal_places=5, max_digits=10)


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
    location = models.ForeignKey(location, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class discharge(models.Model):
    hospital = models.ForeignKey(hospitals, on_delete=models.CASCADE)
    today = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.hospital.name


class death(models.Model):
    hospital = models.ForeignKey(hospitals, on_delete=models.CASCADE)
    today = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.hospital.name


class normal_bed(models.Model):
    hospital = models.ForeignKey(hospitals, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    occupied = models.IntegerField()
    available = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hospital.name


class icu_bed(models.Model):
    hospital = models.ForeignKey(hospitals, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    occupied = models.IntegerField()
    available = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hospital.name


class ventilators(models.Model):
    hospital = models.ForeignKey(hospitals, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    occupied = models.IntegerField()
    available = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hospital.name


class OxygenCylinders(models.Model):
    hospital = models.ForeignKey(hospitals, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    occupied = models.IntegerField()
    available = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hospital.name
