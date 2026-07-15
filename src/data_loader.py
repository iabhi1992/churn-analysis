import pandas as pd
from src.config import DATA_PATH

REQUIRED_COLUMNS = ["customer_id", "last_purchase_date", "total_spend"]
def load_data():
	"""Load the customer dataset from the cofigured path."""
	df = pd.read_csv(DATA_PATH)
	validate_data(df)
	print(f"Loaded {len(df)} rows and {len(df.columns)} columns.")
	return df

df validate_data(df):
	"""Check the dataset meets basic quality expectations."""
	if df.empty:
		raise ValueError("Dataset is empty.")

	missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
	if missing:
		raise ValueError(f"Missing required columns: {missing}")
	if df.isnull().sum().sum() > 0:
		print("Warning: dataset contains missing values.")
	return True
