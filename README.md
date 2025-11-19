# Flask Emergency Alert App

A small Flask-based application that sends emergency SMS alerts to contacts within a specified radius. The app reads contacts from a local SQLite database, geocodes addresses via the Google Maps Geocoding API, and sends SMS messages using Twilio.

## Features

- Contact retrieval from a local SQLite database
- Geocoding addresses (Google Maps Geocoding API)
- Proximity detection (returns contacts within a given distance)
- SMS alert dispatch via Twilio

## Requirements

- Python 3.x
- Flask
- Flask-CORS
- Requests
- SQLite3
- Twilio
- Geopy

(Install packages with `pip install -r requirements.txt` — see Setup below.)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/udy18/flask-emergency-alert-app.git
cd flask-emergency-alert-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure credentials

You can either edit `app.py` to add credentials directly (not recommended), or set environment variables and modify the app to read them. Example environment variables:
```bash
export TWILIO_ACCOUNT_SID="your_account_sid"
export TWILIO_AUTH_TOKEN="your_auth_token"
export TWILIO_PHONE_NUMBER="+1234567890"
export GOOGLE_MAPS_API_KEY="your_api_key"
```

If your current code expects values in `app.py`, add or update the following variables there:
```python
# Twilio account credentials
account_sid = "your_account_sid"
auth_token = "your_auth_token"
twilio_phone_number = "your_twilio_number"

# Google Maps API key
google_maps_api_key = "your_api_key"
```

4. Create the SQLite database

Create a `contacts.db` SQLite database in the project root and populate it with your contacts (phone numbers and addresses). The schema depends on how `app.py` reads contacts—ensure columns match the app's expectations.

5. Start the application:
```bash
python app.py
```

The application runs at:
http://localhost:5000/

## API Endpoints

### GET /
Returns a default message (e.g., "Hello, World!").

Example:
```bash
curl http://localhost:5000/
```

### POST /alert
Sends an alert to contacts within the provided radius from the given coordinates.

Request JSON payload:
```json
{
  "latitude": 12.345678,
  "longitude": 98.765432,
  "max_distance": 5.0
}
```
- latitude: latitude of the requesting user (decimal degrees)
- longitude: longitude of the requesting user (decimal degrees)
- max_distance: maximum distance in kilometers to search for contacts

Example curl request:
```bash
curl -X POST http://localhost:5000/alert \
  -H "Content-Type: application/json" \
  -d '{"latitude": 12.345678, "longitude": 98.765432, "max_distance": 5.0}'
```

Example response (structure may vary depending on implementation):
```json
{
  "contacts": [
    {
      "name": "Alice",
      "phone": "+1234567890",
      "address": "123 Example St, City, Country",
      "distance_km": 2.3
    },
    {
      "name": "Bob",
      "phone": "+1987654321",
      "address": "456 Another Rd, City, Country",
      "distance_km": 4.8
    }
  ],
  "count": 2
}
```

## Notes & Recommendations

- Use environment variables for credentials (Twilio, Google) instead of hardcoding.
- Ensure your Google Maps API key has Geocoding API enabled and request quotas are sufficient.
- Validate phone numbers and addresses during data entry to avoid failed SMS or geocoding calls.
- Consider rate-limiting or authorization on the API to prevent abuse.

## Future Improvements

- User authentication and authorization for sending alerts
- Replace SQLite with a more scalable database (PostgreSQL, MySQL)
- Asynchronous processing (e.g., Celery) for SMS dispatch to improve responsiveness
- Robust error handling and structured logging
- Frontend UI (React, Vue, or Angular) for easier interaction

## License

Add a license if you want to make the repository open source (e.g., MIT, Apache 2.0).
