# Fitness Booking Django API

## Setup & Run in VS Code
1. Open folder in VS Code
2. Create virtualenv (optional): `python -m venv venv && source venv/bin/activate`
3. Install deps: `pip install -r requirements.txt`
4. Make migrations & migrate: `python manage.py makemigrations && python manage.py migrate`
5. Seed sample data: `python manage.py shell < seed.py`
6. Run server: `python manage.py runserver`

## Sample REST API calls

### List classes with timezone
curl 'http://127.0.0.1:8000/api/classes?timezone=US/Eastern'

### Book a class
curl -X POST -H "Content-Type: application/json" -d '{"class_id":1,"client_name":"Rohith","client_email":"rohith@example.com"}' http://127.0.0.1:8000/api/book

### Get bookings
curl 'http://127.0.0.1:8000/api/bookings?email=rohith@example.com'