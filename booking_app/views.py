from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
import pytz

@api_view(['GET'])
def list_classes(request):
    timezone = request.GET.get('timezone', 'Asia/Kolkata')
    try:
        tz = pytz.timezone(timezone)
    except Exception:
        return Response({"error": "Invalid timezone"}, status=400)
    classes = FitnessClass.objects.all()
    for c in classes:
        c.datetime_ist = c.datetime_ist.astimezone(tz)
    serializer = FitnessClassSerializer(classes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_class(request):
    class_id = request.data.get('class_id')
    name = request.data.get('client_name')
    email = request.data.get('client_email')
    if not all([class_id, name, email]):
        return Response({"error": "Missing fields"}, status=400)
    try:
        fclass = FitnessClass.objects.get(id=class_id)
    except FitnessClass.DoesNotExist:
        return Response({"error": "Class not found"}, status=404)
    if fclass.available_slots <= 0:
        return Response({"error": "No slots available"}, status=400)
    booking = Booking(fitness_class=fclass, client_name=name, client_email=email)
    booking.save()
    fclass.available_slots -=1
    fclass.save()
    serializer = BookingSerializer(booking)
    return Response(serializer.data, status=201)

@api_view(['GET'])
def get_bookings(request):
    email = request.GET.get('email')
    bookings = Booking.objects.filter(client_email=email)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)