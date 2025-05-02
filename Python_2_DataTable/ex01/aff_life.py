from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def main():

    # Load the dataset
    life_exp = load("life_expectancy_years.csv")
    life_exp.set_index("country", inplace=True)
	

    
    # Extract the data for Czech Republic, Pandas Series
    czech_life_exp = life_exp.loc["Czech Republic"]
    
    # Extract years (columns) and life expectancy values
    years = czech_life_exp.index.astype(int)  # Convert column names (years) to integers
    print(czech_life_exp.index)
    
	#returns np array
    life_expectancy = czech_life_exp.values   # Extract life expectancy values
    #print(len(years), len(life_expectancy)) #arrays are of the same lenghth == they are aligned

    # Plot the data
    plt.plot(years, life_expectancy) #(x, y)
    plt.title("Czech Republic Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.xticks(np.arange(1800, 2100, 40))
    plt.yticks(np.arange(30, 100, 10))
    plt.show()

if __name__ == "__main__":
	main()