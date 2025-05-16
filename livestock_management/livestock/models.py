from django.db import models
from django.contrib.auth.models import  User


class Animal(models.Model):
    rfid = models.CharField(max_length=50, unique=True, primary_key=True)
    type = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    birthdate = models.DateField()
    registration_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return  f"{self.type} - {self.rfid}"
    

class HealthRecord(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='health_records')
    record_date = models.DateTimeField(auto_now_add=True)
    diagnosis = models.TextField()
    treatment = models.TextField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.animal.rfid} - {self.record_date}"

class ProductivityRecord(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='productivity_records')
    record_date = models.DateField()
    milk_yield = models.FloatField(null=True, blank=True)
    growth_rate = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.animal.rfid} - {self.record_date}"


