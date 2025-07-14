from booking_app.models import FitnessClass
import pytz
from datetime import datetime

tz = pytz.timezone('Asia/Kolkata')

if not FitnessClass.objects.exists():
    FitnessClass.objects.create(name='Yoga', datetime_ist=tz.localize(datetime(2025, 7, 20, 8, 0)), instructor='Alice', available_slots=5)
    FitnessClass.objects.create(name='Zumba', datetime_ist=tz.localize(datetime(2025, 7, 20, 10, 0)), instructor='Bob', available_slots=10)
    FitnessClass.objects.create(name='HIIT', datetime_ist=tz.localize(datetime(2025, 7, 21, 7, 0)), instructor='Charlie', available_slots=8)

print('Seeded!')
