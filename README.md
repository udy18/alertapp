Flask Emergency Alert App

This Flask-based application enables users to send emergency alerts to contacts located within a specified distance. It integrates the Google Maps Geocoding API for address resolution and the Twilio API for delivering SMS notifications.

Features

Contact Retrieval from SQLite Database
Reads phone numbers and addresses from a local SQLite database for processing.

Proximity Detection
Calculates the distance between the user’s current coordinates and each contact’s geocoded location, returning only those within the specified maximum distance.

SMS Alerts via Twilio
Sends emergency SMS messages to contacts identified within the defined radius.

Requirements

Python 3.x

Flask

Flask-CORS

Requests

SQLite3

Twilio

Geopy

Setup

Clone the repository:

git clone https://github.com/udy18/flask-emergency-alert-app.git


Install the required dependencies:

pip install -r requirements.txt


Add your Twilio and Google Maps API credentials in app.py:

# Twilio account credentials
account_sid = "your_account_sid"
auth_token = "your_auth_token"
twilio_phone_number = "your_twilio_number"

# Google Maps API key
google_maps_api_key = "your_api_key"


Create the contacts.db SQLite database in the project root directory.

Start the application:

python app.py


The application will run at:

http://localhost:5000/

API Endpoints
GET /

Returns a default "Hello, World!" message.

POST /alert

Accepts a JSON payload containing:

latitude: Latitude of the requesting user

longitude: Longitude of the requesting user

max_distance: Maximum distance (in kilometers) to search for contacts

The response includes a list of contacts within the specified radius, along with their phone numbers, addresses, and calculated distances.

Future Improvements

User Authentication
Restrict alert-sending operations to verified and authorized users.

Database Enhancement
Replace SQLite with a scalable database (e.g., PostgreSQL or MySQL) for improved performance and reliability.

Asynchronous Processing
Integrate Celery or similar tools to handle SMS dispatch asynchronously and reduce API response times.

Robust Error Handling and Logging
Add structured logging and improved exception handling for diagnostics and stability.

Frontend Integration
Build a frontend interface (React, Angular, or Vue.js) for improved usability and end-user interaction.
