# Flight Deals Tracker

A Python application that monitors flight prices for multiple routes and identifies low-cost travel deals using third-party APIs.

## Features
- Tracks flight prices for multiple origin–destination routes
- Compares prices against user-defined thresholds
- Stores deal information in Google Sheets
- Generates alerts when deal conditions are met

## Tech Stack
- Python
- REST APIs
- JSON
- Google Sheets

## How It Works
1. Fetches flight pricing data via APIs  
2. Parses JSON responses per route  
3. Compares current prices with thresholds  
4. Logs and updates deal information  

## Usage
- Configure routes and price limits
- Run the script to check for deals

## Future Improvements
- Add email or WhatsApp notifications
- Extend support for more airlines
