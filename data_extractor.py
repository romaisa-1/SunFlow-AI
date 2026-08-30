def extract_environment_data(response_data):
    location = response_data["data"]["result"]["locations"][0]

    parameters = location["parameters"]
    solar = location["solar_irradiance"]["clear_sky"]

    data = {
        "latitude": location["lat"],
        "longitude": location["lon"],
        "elevation": location["elevation"],
        "temperature": location["temperature"],
        "heat_index": parameters["heat_index_celsius"][0],
        "apparent_temperature": parameters["apparent_temperature_celsius"][0],
        "humidity": parameters["relative_humidity_percent"][0],
        "precipitation": parameters["precipitation_mm"][0],
        "ghi": solar["ghi"],
        "dni": solar["dni"],
        "dhi": solar["dhi"],
    }

    return data