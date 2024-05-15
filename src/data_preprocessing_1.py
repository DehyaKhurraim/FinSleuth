import pandas as pd
import numpy as np
import json
import csv
import logging
from random import randint
import tkinter as tk
from tkinter import filedialog
import pandas as pd

def open_csv_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if file_path:
        # Read the CSV file using pandas
        df = pd.read_csv(file_path)
        print("CSV File Selected:", file_path)
        # print(df.head())  # Display the first few rows of the CSV data
    
    return file_path  # Return the file_path variable

# Function call to open the file dialog and get the file_path
data_path = open_csv_file()

# Check if a file was selected
if data_path:
    # You can use the selected_file variable here
    print("Selected file path:", data_path)
else:
    print("No file selected.")


# data_path = "data/data.csv"

logging.basicConfig(filename='C:\\New folder\\aml-repo\\logs\\model_development.txt',
					filemode='a',
					format='%(asctime)s %(message)s',
					datefmt="%Y-%m-%d %H:%M:%S")

logging.warning("DATA PREPROCESSING 1 STAGE")

logging.warning("Reading Dataset...")

X = pd.read_csv(data_path)
X = X.to_numpy()

logging.warning("Read Dataset")

nameOrigCol = 3
nameDestCol = 6
nameOrig = []
nameDest = []
nameCount = {}
namesWithMoreThanOneOccurrence = []

logging.warning("Checking Each Person's Transactions Count...")

for name in X[:,nameOrigCol]:
	if nameCount.get(name,-1) == -1:
		nameOrig.append(name)

		nameCount[name] = 1

	else:
		nameCount[name] += 1
		namesWithMoreThanOneOccurrence.append(name)

for name in X[:,nameDestCol]:
	if nameCount.get(name,-1) == -1:
		nameDest.append(name)

		nameCount[name] = 1

	else:
		nameCount[name] += 1
		namesWithMoreThanOneOccurrence.append(name)

logging.warning("Count Identification Done")

logging.warning("Calculating Median ...")

countArr = []
count = 0
for attr, value in nameCount.items():
	if value>40:
		countArr.append(value)
		count += 1
median = np.median(countArr)

logging.warning(f"Median : {median}")

logging.warning("Filtering Data Based on Transactions Count...")
csv_golden_data = []

for i in range(X.shape[0]):
	if nameCount.get(X[i,3],-1) > 40 or nameCount.get(X[i,6],-1) > 40:
		csv_golden_data.append(X[i,:])

logging.warning("Filtering Done")

logging.warning("Storing Filtered Data in data_processed folder...")

with open("C:\\New folder\\aml-repo\\data_processed/filtered_data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(csv_golden_data)

logging.warning("Data is Stored")

print("data preprocessing 1 run successfully")



