""" Loads the CSV file and filters to components of interest. """

# External imports
import pandas as pd

def load_data(csv_file):
    """ Loads the CSV file and filters to components of interest. """

    df = pd.read_csv(csv_file, usecols=("Material: Name","Company name","Construction times","Average cost/cubic metre","Overall EC sum (tonCO2e)"))

    return df


def create_score(df, money_weight=100, eco_weight=100, speed_weight=100):
    """ Basic scoring system. """
    print(df)

    df2 = pd.DataFrame(df["Material: Name"])
    df2.insert(1, "Company name", df["Company name"])

    df2["money_score"] = round(100 - (df["Average cost/cubic metre"]/2), 0).astype(int)

    df2["eco_score"] = round(100 - (df["Overall EC sum (tonCO2e)"] * 10000),0).astype(int)

    df2["speed_score"] = df["Construction times"] * 10
    print(df2)

    df2["overall_score"] = ((df["money_score"]*money_weight) + (df["eco_score"]*eco_weight) + (df["speed_score"]*speed_weight)) /  (money_weight + eco_weight + speed_weight)
    # print(df2)
    return df2

df = load_data("static/data/concrete.csv")
df = create_score(df, money_weight=100, eco_weight=100, speed_weight=100)