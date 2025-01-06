import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the CSV file

csv_file = os.path.join(os.getcwd(), 'data/Anexos_7/results.csv')
data = pd.read_csv(csv_file)

# Set the 'Date' column as the index
data['Date'] = pd.to_datetime(data['Date'], format='%Y_%m_%d')
data.set_index('Date', inplace=True)

# Plot the data
plt.figure(figsize=(12, 6))

for province in data.columns:
    plt.plot(data.index, data[province], marker='o', label=province)

plt.title('Daily Incomes by Province')
plt.xlabel('Date')
plt.ylabel('Incomes')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()
