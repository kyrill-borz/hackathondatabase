""" Loads the CSV file and filters to components of interest. """

__author__ = "Eve Sherratt, John Jessop"

# Standard library imports
import json

# External imports
import numpy as np
import pandas as pd
from calculate_flight_distance import calculate_flight_distance

# Constants
EARTH_RADIUS = 6.371e6 # Average radius of the Earth in metres

# Code
def load_data(csv_file):
    """ Loads the CSV file and filters to components of interest. """

    df = pd.read_csv(csv_file, usecols=("Material: Name","Company name","Construction times","Average cost/cubic metre","Overall EC sum (tonCO2e)"))

    return df


def create_score(df, money_weight, eco_weight, speed_weight, longitude, latitude):
    """ Basic scoring system. """

    df2 = pd.DataFrame(df["Material: Name"])
    df2.insert(1, "Company name", df["Company name"])

    df2["Money score (%)"] =  (100 - (df["Average cost/cubic metre"]/2)).round().astype(int)

    df2["Eco score (%)"] = (100 - (df["Overall EC sum (tonCO2e)"] * 10000)).round().astype(int)

    df2["Speed score (%)"] = df["Construction times"] * 10

    df2["Distance (m)"] = calculate_flight_distance("static/data/company_data.json", "A", longitude, latitude)

    total_weight = int(money_weight) + int(eco_weight) + int(speed_weight)
    df2["Overall score (%)"] = (((df2["Money score (%)"]*int(money_weight)) + (df2["Eco score (%)"]*int(eco_weight)) + (df2["Speed score (%)"]*int(speed_weight))) /  total_weight).round().astype(int)

    return df2

def calculate_flight_distance(location_json, company_name, user_latitude, user_longitude):
    """ Crude algorithm to calculate a flight distance from a factory to the user's construction location. """

    # Load company location
    with open(location_json, 'r') as json_file:
        location_data = json.load(json_file)
        print(location_data)

    company_latitude = location_data[company_name]["latitude"]
    company_longitude = location_data[company_name]["longitude"]

    # Convert to radians for use in numpy
    from_latitude = np.deg2rad(company_latitude)
    from_longitude = np.deg2rad(company_longitude)
    to_latitude = np.deg2rad(user_latitude)
    to_longitude = np.deg2rad(user_longitude)

    # Auxilliary length quantities, all in metres
    from_point_radius = 15240 + EARTH_RADIUS # Assuming 15240m is cruising altitude
    to_points_radius = 15240 + EARTH_RADIUS
    longitude_diff = to_longitude - from_longitude

    # Angle(s) subtended at centre of Earth, in radians
    cos_central_angle = np.real(
        np.sin(to_latitude) * np.sin(from_latitude)
        + np.cos(to_latitude) * np.cos(from_latitude)
        * np.cos(longitude_diff))

    # Calculate return quantities
    distance = np.sqrt(from_point_radius**2 + to_points_radius**2
        - 2 * from_point_radius * to_points_radius * cos_central_angle)

    return distance
