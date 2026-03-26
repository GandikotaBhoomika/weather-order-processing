import json
import asyncio
import aiohttp
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Load orders
with open("orders.json", "r") as file:
    orders = json.load(file)

# Fetch weather
async def fetch_weather(session, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    try:
        async with session.get(url) as response:
            data = await response.json()
            return city, data
    except Exception as e:
        return city, {"error": str(e)}

# Generate apology message
def generate_apology(order, condition):
    return f"Hi {order['customer']}, your order to {order['city']} is delayed due to {condition}. We appreciate your patience!"

# Process orders
async def process_orders():
    async with aiohttp.ClientSession() as session:
        tasks = []

        for order in orders:
            city = order["city"]
            tasks.append(fetch_weather(session, city))

        results = await asyncio.gather(*tasks)

        for city, data in results:
            for order in orders:
                if order["city"] == city:

                    if "weather" in data:
                        condition = data["weather"][0]["main"]

                        if condition in ["Rain", "Snow", "Extreme", "Clouds", "Clear"]:
                            order["status"] = "Delayed"
                            print(generate_apology(order, condition))

                    else:
                        print(f"Error fetching weather for {city}")

# Run
asyncio.run(process_orders())

# Save updated orders
with open("orders_updated.json", "w") as file:
    json.dump(orders, file, indent=2)