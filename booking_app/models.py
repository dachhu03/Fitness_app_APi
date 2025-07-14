from django.db import models

class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    datetime_ist = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    available_slots = models.IntegerField()

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, related_name='bookings', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()