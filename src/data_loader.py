import pandas as pd
from src.config import DATA_PATH

def load_data():
	"""Load the customer dataset from the configured path."""
	df = pd.read_csv(DATA_PATH)
	validate_data(df)
	print(f"Loaded {len(df)} rows and {len(df.columns)} columns.")
	return df

def validate_df(df):
	"""Check the dataset meets basic quality expecttations."""
	if df.empty:
		raise ValueError("Dataset is empty.")
	if df.isnull().sum() > 0:
		print("Warning: dataset contains missing values.")
	return True
