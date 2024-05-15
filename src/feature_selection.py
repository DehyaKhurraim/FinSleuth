import numpy as np
import pandas as pd
import logging
from sklearn.ensemble import RandomForestClassifier 
from sklearn.preprocessing import OneHotEncoder

logging.basicConfig(filename='logs/model_development.txt',
                    filemode='a',
                    format='%(asctime)s %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

logging.warning("----------")
logging.warning("FEATURE SELECTION STAGE")

logging.warning("Reading Filtered Data 3 ...")

dataframeX = pd.read_csv('data_processed/filtered_data_3.csv')
col_names = list(dataframeX.columns.values)
dataMat = dataframeX.to_numpy()

logging.warning("Read Filtered Data 3")

logging.warning("Reading Association Rules Data...")

association_rules_data = pd.read_csv('reports/association_rules.csv')

# Extract antecedents and consequents
antecedents = association_rules_data['antecedents']
consequents = association_rules_data['consequents']

# Convert frozenset strings to lists
antecedents = antecedents.apply(lambda x: list(eval(x)))
consequents = consequents.apply(lambda x: list(eval(x)))

# Combine antecedents and consequents into a single column
association_rules_data['features'] = antecedents + consequents

# Use one-hot encoding to convert categorical features into a binary matrix
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X_association = encoder.fit_transform(association_rules_data['features'].apply(lambda x: pd.Series(x)).values)

# Assuming some target variable for Y, you may need to adjust this based on your use case
Y_association = association_rules_data['confidence']

logging.warning(f"Shape of X_association: {X_association.shape} and Shape of Y_association: {Y_association.shape}")

logging.warning("Instiantiating Random Forest Classifier Model...")

model = RandomForestClassifier(random_state=42)  # Use RandomForestClassifier

logging.warning("Fitting Data...")

model.fit(X_association, Y_association.astype(int))

logging.warning("Checking Feature Importances...")

feature_imp = model.feature_importances_

logging.warning("Feature Importances: ")

fea_imp = []

for i in range(len(feature_imp)):
    if i + 2 < len(col_names):  # Check if the index is within bounds
        fea_imp.append([col_names[i + 2], feature_imp[i]])

logging.warning("Storing Feature Importances in reports...")

features = pd.DataFrame(fea_imp, columns=["features", "importance_score"])
features.to_csv("reports/feature_importances_rf.csv", index=False) 
logging.warning("Storing Feature Importances Done")
print("feature selection run successfully")