# Flask Emergency Alert App — Product Case Study (PM Intern)

A lightweight Flask service that sends emergency SMS alerts to contacts within a configurable geographic radius using Google Geocoding and Twilio.

## Problem statement
In emergencies, people need a fast way to notify nearby trusted contacts. Many existing solutions are mobile-only, require pre-configured groups, or have high setup friction. This backend demo shows a minimal workflow to locate contacts by proximity and dispatch SMS alerts quickly.

## Target users
- Individuals who want a one-tap emergency notification to nearby friends/family.
- Community organizers or small teams managing contact lists.
- Developers prototyping emergency features.

## Core value proposition
Automatically surface and notify contacts who are physically close to the user, reducing time to inform and increasing the chances of receiving timely help.

## Product goals (MVP)
1. Accuracy — identify contacts within a configurable radius reliably.
2. Reliability — ensure SMS dispatch with retry and error reporting.
3. Privacy & Safety — prevent accidental or unauthorized broadcasts.
4. Speed — keep end-to-end alert <= 10s for typical datasets.

## Suggested success metrics
- Matching accuracy for proximity (target: >90% within 5km).
- End-to-end alert latency (target: <10s for <50 recipients).
- SMS delivery rate after retries (target: >=98%).
- Percent of false-positive alerts (target: <1% in initial 1000 uses).

## What’s implemented (core features)
- Contacts stored in a local SQLite database.
- Address geocoding via Google Maps Geocoding API.
- Distance calculation (Haversine) to filter contacts within max_distance.
- SMS delivery using Twilio.
- Minimal REST API: GET / and POST /alert.

## High-level flow
1. Client sends current lat/lon and radius to POST /alert.  
2. Backend geocodes stored addresses (cached where possible).  
3. Backend filters contacts by distance and returns matches.  
4. Twilio sends SMS to matched numbers.  
5. Backend returns summary of successes/failures.

## Architecture summary
- App: Flask (single-process MVP)
- Storage: SQLite (contacts.db)
- External: Google Geocoding API, Twilio REST API
- Geolocation helper: geopy / Haversine

Tradeoffs
- SQLite: low friction but limited scalability and concurrency.
- Synchronous SMS dispatch: easy to implement, but increases latency; background processing recommended for production.

## Developer setup (quick)
1. Clone:
```bash
git clone https://github.com/udy18/alertapp.git
cd alertapp
```
2. Install:
```bash
pip install -r requirements.txt
```
3. Provide credentials (prefer env vars):
```bash
export TWILIO_ACCOUNT_SID="your_account_sid"
export TWILIO_AUTH_TOKEN="your_auth_token"
export TWILIO_PHONE_NUMBER="+1234567890"
export GOOGLE_MAPS_API_KEY="your_api_key"
```
4. Ensure contacts.db exists with expected columns (name, phone, address).
5. Run:
```bash
python app.py
```
6. Example call:
```bash
curl -X POST http://localhost:5000/alert \
  -H "Content-Type: application/json" \
  -d '{"latitude": 12.345678, "longitude": 98.765432, "max_distance": 5.0}'
```


## Recommended roadmap (0–6 months)
Short (0–1m)
- Move SMS delivery to async queue (Celery/Redis).
- Add retry/backoff and DLQ handling.

Mid (1–3m)
- Replace SQLite with PostgreSQL and add migrations.
- Add basic admin UI to manage contacts and review alert logs.

Long (3–6m)
- Add user authentication and contact opt-in verification.
- Multi-channel notifications (push/email), analytics dashboard.

## Risks & mitigation
- Incorrect geocoding → add manual address validation and user confirmations.
- Unintended alerts → require confirmation step or two-step escalate flow.
- Regulatory/privacy concerns → minimize retention and implement opt-in consent.



