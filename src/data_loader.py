import pandas as pd
from src.config import DATA_PATH


def load_data():
	"""Load the customer dataset from the configured path."""
	df = pd.read_csv(DATA_PATH)
	print(f"Loaded {len(df)} rows and {len(def.columns)} columns.")
	return df
