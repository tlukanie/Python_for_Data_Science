from load_csv import load
import matplotlib.pyplot as plt
import numpy as np

def main():
	try:
		loaded_data = load("population_total.csv")
	except Exception as e:
		print(f"{type(e).__name__}: {e}")
	try:
		loaded_data.set_index("country", inplace=True)
		czech_data = loaded_data.loc["Czech Republic"]
		ukraine_data = loaded_data.loc["Ukraine"]
		years = czech_data.index.astype(int)
		filtered_years = [year for year in years if year <= 2050]
		print(czech_data.dtype)
		cz_pop = czech_data.str.replace('M', '').astype(float)
		ukr_pop = ukraine_data.str.replace('M', '').astype(float)
		filtered_cz_values = cz_pop[:len(filtered_years)]
		filtered_ukr_values = ukr_pop[:len(filtered_years)]
		print(cz_pop.dtype)

		plt.plot(filtered_years, filtered_cz_values, label="Czech Republic")
		plt.plot(filtered_years, filtered_ukr_values, color='green', label="Ukraine")
		plt.title("Population Projections")
		plt.xlabel("Year")
		plt.ylabel("Population")
		plt.xticks(np.arange(1800, 2050, 40))
		plt.yticks([20, 40, 60], ['20M', '40M', '60M'])
		plt.ylim(0, 70)
		plt.legend()
		plt.show()
	except Exception as e:
		print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
	main()