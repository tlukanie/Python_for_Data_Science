from load_csv import load
import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd

def main():
	try:
		income_per_person = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
		life_expectancy = load("life_expectancy_years.csv")
	except Exception as e:
		print(f"{type(e).__name__}: {e}")
		sys.exit(1)
	try:
		income_per_person.set_index("country", inplace=True)
		life_expectancy.set_index("country", inplace=True)
		combined = pd.DataFrame({
			"income": income_per_person["1900"],
			"life_expectancy": life_expectancy["1900"]
		})
		print(combined)
		# drop rows with NaN values in either column
		combined.dropna(inplace=True)
		
		# Extract cleaned data
		incm_v = combined["income"].values
		lf_exp_v = combined["life_expectancy"].values
		plt.plot(incm_v, lf_exp_v, 'o')
		plt.title("1900")
		plt.ylabel("Life Expectancy")
		plt.xlabel("Gross domestic product")
		plt.xscale('log')
		plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
		plt.xlim(300, 10100)
		plt.show()
	except Exception as e:
		print(f"{type(e).__name__}: {e}")
	

if __name__ == "__main__":
	main()