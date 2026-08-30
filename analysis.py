def calculate_heat_risk(heat_index):
    if heat_index < 27:
        return "Low"
    elif heat_index < 32:
        return "Moderate"
    elif heat_index < 41:
        return "High"
    else:
        return "Very High"


def calculate_solar_availability(ghi):
    if ghi < 200:
        return "Low"
    elif ghi < 500:
        return "Moderate"
    else:
        return "Strong"


def analyze_environment(environment):
    heat_risk = calculate_heat_risk(environment["heat_index"])
    solar_availability = calculate_solar_availability(environment["ghi"])

    return {
        "heat_risk": heat_risk,
        "solar_availability": solar_availability,
    }