""" Crude algorithm to calculate a flight distance from a factory to the user's construction location. """

__author__ = "Eve Sherratt"

# Standard library imports
import json

# External imports
import numpy as np

# Constants
EARTH_RADIUS = 6.371e6 # Average radius of the Earth in metres

# Code

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

from basic_algorithm import load_data
df = load_data("static/data/concrete.csv")
dist = calculate_flight_distance("static/data/company_data.json", "A", 88, 32)
