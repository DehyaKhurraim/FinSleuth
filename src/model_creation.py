import numpy as np
import pandas as pd
import pickle
import json
from datetime import datetime
import logging
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
# from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, f1_score, recall_score, precision_score

logging.basicConfig(filename='logs/model_development.txt',
                    filemode='a',
                    format='%(asctime)s %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

logging.warning("Reading Final Dataset...")

data_path = "data_processed/filtered_data_3.csv"
dataMat = pd.read_csv(data_path)

logging.warning("Read Final Dataset")

# Read the entity column from the data.csv file
entity_data = pd.read_csv("data/data.csv")

logging.warning("Creating X and y variables ...")

# Selecting features excluding 'isFraud'
X = dataMat.drop(columns=['isFraud'])
y = dataMat['isFraud']

logging.warning(f"Shape of X: {X.shape} and Shape of y: {y.shape}")

logging.warning("Splitting Dataset...")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Load feature importances
feature_importances = pd.read_csv("reports/feature_importances_rf.csv")

# Sort feature importances in descending order
feature_importances.sort_values(by='importance_score', ascending=False, inplace=True)

# Use the most important feature for predicting fraud
most_important_feature = feature_importances.iloc[0]['features']

# Calculate the mean and standard deviation of the most important feature
mean_feature = X_test[most_important_feature].mean()
std_feature = X_test[most_important_feature].std()

# Set the threshold as mean + 2 standard deviations
threshold = mean_feature + 2 * std_feature

# Display suspicious transactions
suspicious_transactions_xgb = X_test[X_test[most_important_feature] > threshold]
suspicious_transactions_xgb['fraudPrediction'] = 1
# Save suspicious transactions to CSV

if 'Unnamed: 0' in suspicious_transactions_xgb.columns:
    suspicious_transactions_xgb.drop(columns=['Unnamed: 0'], inplace=True)
suspicious_transactions_xgb.to_csv("reports/suspicious_transactions.csv", index=False)

matched_transactions_orig = pd.merge(suspicious_transactions_xgb, entity_data, left_on='entity', right_on='nameOrig', how='inner')

matched_transactions_dest = pd.merge(suspicious_transactions_xgb, entity_data, left_on='entity', right_on='nameDest', how='inner')

# Combine the matched transactions from both nameOrig and nameDest
matched_transactions = pd.concat([matched_transactions_orig, matched_transactions_dest], ignore_index=True)

# Drop duplicates if there are any, keeping only the first occurrence of nameDest
matched_transactions.drop_duplicates(subset='nameDest', keep='first', inplace=True)

# Add an 'isFraud' column and set its value to 1 for all matched transactions
matched_transactions['isFraud'] = 1

# Save matched transactions to CSV files
matched_transactions.to_csv("reports/matched_transactions.csv", index=False)
