import os
import requests
import time
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from data_extractor import extract_environment_data
from analysis import analyze_environment

load_dotenv()


def get_coordinates(destination):
    geolocator = Nominatim(user_agent="sunflow_ai")
    location = geolocator.geocode(destination)

    if not location:
        return None

    return location.latitude, location.longitude
def get_fortyguard_data(latitude, longitude, temperature, start_date, start_time):
    api_key = os.getenv("FORTYGUARD_API_KEY")

    url = "https://api.fortyguard.com/v1/env_params"

    headers = {
        "api-key": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "latitude": latitude,
        "longitude": longitude,
        "temperature": temperature,
        "date_time": {
            "start_date": start_date,
            "start_time": start_time,
            "filter_type": 1
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    return response.json()

def wait_for_result(activity_id):
    api_key = os.getenv("FORTYGUARD_API_KEY")

    url = f"https://api.fortyguard.com/v1/status/{activity_id}"

    headers = {
        "api-key": api_key
    }

    for _ in range(10):
        response = requests.get(url, headers=headers)
        result = response.json()

        status = result["data"]["status"]

        if status == "Completed":
            return result

        time.sleep(2)

    return None


def analyze_destination(
    destination,
    temperature,
    start_date,
    start_time
):
    coordinates = get_coordinates(destination)

    if not coordinates:
        return None

    latitude, longitude = coordinates

    submitted = get_fortyguard_data(
        latitude,
        longitude,
        temperature,
        start_date,
        start_time
    )

    activity_id = submitted["data"]["activity_id"]

    result = wait_for_result(activity_id)

    if not result:
        return None

    environment = extract_environment_data(result)

    analysis = analyze_environment(environment)

    return {
        "environment": environment,
        "analysis": analysis
    }