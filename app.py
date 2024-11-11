from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import sqlite3
from twilio.rest import Client
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import os

# Twilio account credentials
account_sid = 'account_sid'
auth_token = 'auth_token'
twilio_phone_number = 'number'

# Google Maps API key
google_maps_api_key = 'MYAPIKEY'

# SQLite database file
sqlite_db_file = 'contacts.db'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Initialize geocoder
geolocator = Nominatim(user_agent="my_app")

def get_coordinates(address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={google_maps_api_key}"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    return None

def get_contacts_from_sqlite():
    conn = sqlite3.connect(sqlite_db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT phone, address FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    return contacts

def get_users_within_distance(current_location, max_distance):
    contacts = get_contacts_from_sqlite()
    users_within_distance = []

    for contact in contacts:
        number, address = contact
        if number and address:
            contact_coords = get_coordinates(address)
            if contact_coords:
                distance = geodesic(current_location, contact_coords).kilometers
                if distance <= max_distance:
                    users_within_distance.append({
                        'phone': number,
                        'address': address,
                        'distance': distance
                    })

    return users_within_distance

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 
@app.get("/")
def default_route():
    print("Works")  # This will print to the console when the route is accessed
    return jsonify({"message": "Hello, World!"}), 200  # Returning a JSON response

@app.post("/alert")
def alert_users():
    data = request.json
    if 'latitude' not in data or 'longitude' not in data or 'max_distance' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        latitude = data['latitude']
        longitude = data['longitude']
        max_distance = data['max_distance']

        if not isinstance(max_distance, (int, float)) or not isinstance(latitude, (int, float)) or not isinstance(longitude, (int, float)):
            return jsonify({'error': 'Invalid data types'}), 400

        current_location = (latitude, longitude)
        users_within_distance = get_users_within_distance(current_location, max_distance)

        return jsonify({'users': users_within_distance}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
