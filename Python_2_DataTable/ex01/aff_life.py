from load_csv import load
import matplotlib.pyplot as plt
import numpy as np
import sys


def main():
	try:
		# Load the dataset
		life_exp = load("life_expectancy_years.csv")
	except Exception as e:
		print(f"Error loading provided file: {e}")
		sys.exit(1)
	try:
		life_exp.set_index("country", inplace=True)
		
		# Extract the data for Czech Republic, Pandas Series
		czech_life_exp = life_exp.loc["Czech Republic"]
		# ukr_life_exp = life_exp.loc["Ukraine"]
		# ukr_y = ukr_life_exp.values
		# Extract years (columns) and life expectancy values
		years = czech_life_exp.index.astype(int)  # Convert column names (years) to integers
		# print(czech_life_exp.index)
		#returns np array
		life_expectancy = czech_life_exp.values   # Extract life expectancy values
		#print(len(years), len(life_expectancy)) #arrays are of the same lenghth == they are aligned
		# Plot the data
		plt.plot(years, life_expectancy) #(x, y)
		# plt.plot(years, ukr_y, color='green', label='Ukraine')
		plt.title("Czech Republic Life Expectancy Projections")
		plt.xlabel("Year")
		plt.ylabel("Life Expectancy")
		plt.xticks(np.arange(1800, 2100, 40))
		plt.yticks(np.arange(30, 100, 10))
		plt.ylim(25, 95)
		plt.show()
	except Exception as e:
		print(f"Error displaying data: {e}")

if __name__ == "__main__":
	main()