""" Loads the CSV file and filters to components of interest. """

# External imports
import pandas as pd

def load_data(csv_file):
    """ Loads the CSV file and filters to components of interest. """

    df = pd.read_csv(csv_file, usecols=("Material: Name","Company name","Overall EC sum (tonCO2e)"))

    return df