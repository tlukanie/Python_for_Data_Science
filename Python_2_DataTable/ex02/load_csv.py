import pandas as pd


def load(path: str) -> pd.DataFrame:
	try:
		data_set = pd.read_csv(path)
		print("Loading dataset of dimensions ",end='')
		print(data_set.shape)
		return data_set
	except Exception as e:
		print(f"Error: {e}")
		return
