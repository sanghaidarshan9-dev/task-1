import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
# (Make sure the CSV is in the same folder as this script)
file_path = "API_SP.POP.TOTL_DS2_en_csv_v2_174326.csv"

# The first 4 rows are metadata, so skip them
df = pd.read_csv(file_path, skiprows=4)

# Display first few rows to confirm data loaded
print(df.head())

# Select population data for year 2024
population_2024 = df["2024"]

# Remove missing values
population_2024 = population_2024.dropna()

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(population_2024, bins=20)

# Add labels and title
plt.title("Distribution of Population of Countries (2024)")
plt.xlabel("Population")
plt.ylabel("Number of Countries")

# Show grid
plt.grid(True)

# Display the chart
plt.show()
