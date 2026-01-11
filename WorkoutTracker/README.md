# Workout Tracker

Workout Tracker is a Python-based automation tool that logs workout activities by processing natural language exercise input and storing structured workout data in Google Sheets.

---

## Features

- Accepts natural language input for workout logging  
- Extracts exercise name, duration, and calories burned  
- Automatically records workout data with date and time  
- Stores workout history in Google Sheets for tracking  
- Supports multiple exercises in a single session  

---

## Tech Stack

- Python  
- Requests  
- REST APIs  
- JSON  
- Google Sheets  

---

## How It Works

1. Accepts exercise details as natural language input  
2. Sends data to a fitness API for exercise analysis  
3. Parses exercise name, duration, and calories from the response  
4. Logs workout data with timestamps into Google Sheets  

---

## Usage

- Configure API credentials and Google Sheets endpoint in the script  
- Run the script and enter workout details when prompted  
- Review logged workout history in Google Sheets  

---

## Future Improvements

- Add data visualization for workout analytics  
- Support multiple users  
- Secure API keys using environment variables  