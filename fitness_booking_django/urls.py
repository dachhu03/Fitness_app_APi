from django.urls import path, include
urlpatterns = [
    path('api/', include('booking_app.urls')),
]