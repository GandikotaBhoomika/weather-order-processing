# 🌦️ Weather-Based Order Processing System

## 📌 Overview
This project processes customer orders by checking real-time weather conditions using the OpenWeatherMap API.  
If adverse weather conditions are detected, the order status is updated to "Delayed".

---

## 🚀 Features
- ✅ Parallel API calls using asyncio
- ✅ Real-time weather data integration
- ✅ Automatic order status updates
- ✅ Error handling for invalid cities
- ✅ JSON input and output processing

---

## 🛠️ Technologies Used
- Python
- asyncio
- aiohttp
- dotenv
- OpenWeatherMap API

---

## 📂 Project Structure
├── main.py
├── orders.json
├── orders_updated.json
├── .env
└── README.md
