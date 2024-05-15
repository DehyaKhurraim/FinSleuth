# 💰💰 Money Laundering Detection


## 💡 Problem Statement:

The financial sector faces an escalating challenge in combating money laundering, with traditional Anti-Money Laundering (AML) systems struggling to keep pace with evolving illicit financial activities. Static rule-based alert systems often generate a high number of false positives, leading to increased operational costs and inefficiencies in the review process. There is a critical need for a dynamic solution that enhances the accuracy of identifying suspicious transactions while minimizing false positives.

## 📝 Proposed Solution:

Developing a Machine Learning model to classify transactions as Fraud or Not Fraud, the solution aims to identify invisible transaction behavior, detect aberrations, and reduce overall AML system costs by mitigating false positives.

This solution can able to:

- Identification of Currently Invisible Transaction Behavior
- Detection of Aberrations in Transactions
- Mitigation of False Positives in AML Systems

## ⏳ Data Description

Dataset available in kaggle: [PaySim](https://www.kaggle.com/ealaxi/paysim1)

We used `PaySim synthetic dataset` to train our ML model. It is based on a sample of real transactions extracted from one month of financial logs from a mobile money service implemented in an African country.

The original logs were provided by a multinational company, who is the provider of the mobile financial service which is currently running in more than 14 countries all around the world. This synthetic dataset is scaled down 1/4 of the original dataset.

This dataset contains `6362620` Transaction records with `11` features.

## ⽊ Project Tree Structure

```
├── data
│   ├── data.csv
├── data_processed
│   ├── filtered_data.csv
│   ├── filtered_data_2.csv
│   ├── filtered_data_3.csv
├── logs
│   ├── model_development.txt
├── reports
│   ├── association_rules.csv
│   ├── feature_importances.csv
│   ├── missing_values.csv
│   ├── performance.json
│   ├── suspicious_transaction.csv
├── src
│   ├── data_preprocessing_1.py
│   ├── data_preprocessing_2.py
│   ├── data_preprocessing_3.py
│   ├── rule_mining.py
│   ├── dbconnection.py
│   ├── feature_selection.py
│   ├── model_creation.py
├── templates
│   ├── index.html
├── Procfile
├── app.py
├── requirements.txt
└── README.md
```

## 🛠 Tools used

Python programming language and frameworks.

- Visual Studio Code is used as an IDE.
- Front end development is done using HTML/CSS.
- Flask framework is used for backend development.
- BitBucket is used as a version control system.
- PowerBi for Graphical Representations

