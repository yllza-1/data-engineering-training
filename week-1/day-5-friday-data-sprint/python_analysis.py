import pandas as pd

def load_data():
    """Load the orders dataset."""
    df = pd.read_csv("data/orders.csv")
    return dfs