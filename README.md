# Flask Emergency Alert App

This is a Flask web application that allows users to send emergency alerts to other users within a specified distance. The app uses the Google Maps API for geocoding addresses and the Twilio API for sending SMS alerts.

## Features

1. **Fetch Contacts from SQLite Database**: The app reads contact information (phone number and address) from a SQLite database.
2. **Locate Users within a Distance**: The app calculates the distance between the user's current location and the contacts' locations, and returns a list of users within the specified maximum distance.
3. **Send SMS Alerts via Twilio**: The app uses the Twilio API to send SMS alerts to the users within the specified distance.

## Requirements

- Python 3.x
- Flask
- Flask-CORS
- Requests
- SQLite3
- Twilio
- Geopy

## Setup

1. Clone the repository:
```
git clone https://github.com/udy18/flask-emergency-alert-app.git
```

2. Install the required packages:
```
pip install -r requirements.txt
```

3. Set the Twilio and Google Maps API credentials in the `app.py` file:
```python
# Twilio account credentials
account_sid = 'account_sid'
auth_token = 'auth_token'
twilio_phone_number = 'number'

# Google Maps API key
google_maps_api_key = 'MYAPIKEY'
```

4. Create the SQLite database file `contacts.db` in the root directory of the project.

5. Run the app:
```
python app.py
```

The app will start running on `http://localhost:5000/`.

## API Endpoints

1. `GET /`: Default route, returns a "Hello, World!" message.
2. `POST /alert`: Accepts a JSON payload with the following fields:
   - `latitude`: The latitude of the user's current location.
   - `longitude`: The longitude of the user's current location.
   - `max_distance`: The maximum distance (in kilometers) to search for other users.

   The endpoint returns a JSON response with a list of users within the specified distance, including their phone number, address, and distance from the user.

## Future Improvements

1. **User Authentication**: Implement user authentication to ensure only authorized users can send alerts.
2. **Improved Database Design**: The current design uses a simple SQLite database. Consider using a more robust database system like PostgreSQL or MySQL for better scalability and performance.
3. **Asynchronous Processing**: Use asynchronous processing (e.g., Celery, RabbitMQ) to handle the Twilio API calls and reduce the response time of the `/alert` endpoint.
4. **Error Handling and Logging**: Improve error handling and logging for better debugging and troubleshooting.
5. **Frontend Integration**: Develop a frontend application (e.g., using React, Angular, or Vue.js) to provide a user-friendly interface for the app.