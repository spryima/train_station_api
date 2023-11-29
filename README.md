# Train Station API Service

## Overview
The Train Station API Service is a comprehensive solution for managing trains, journeys, stations, and ticket bookings. Designed to simplify and enhance the train travel experience, it allows for efficient trip planning and ticket management.

## Features
- **Station Management**: Details of train stations including location coordinates and associated routes.
- **Train Management**: Information regarding train types, cargo capacity, and seating arrangements.
- **Journey Planning**: Routes, schedules, and real-time updates on train journeys.
- **Ticket Booking**: Simplify the process of booking tickets for passengers.
- **Order Management**: Efficient handling of ticket orders from creation to completion.

## Getting Started

### Prerequisites
- Python 3.8+
- Django 3.2+
- Django Rest Framework

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/spryima/train_station_api
   cd train-station-api

Install required packages:
```python
pip install -r requirements.txt
```

Set up the database:
```python
python manage.py makemigrations
python manage.py migrate
```

Create a superuser:
```python
python manage.py createsuperuser
```

Run the development server:
```python
python manage.py runserver
```



Visit http://127.0.0.1:8000/ in your browser.


API Documentation
For detailed API documentation, visit:

- Swagger UI: http://127.0.0.1:8000/api/doc/swagger/
- Redoc: http://127.0.0.1:8000/api/doc/redoc/


License
Distributed under the MIT License. See LICENSE for more information.