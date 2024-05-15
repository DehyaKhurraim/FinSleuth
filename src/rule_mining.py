import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules
from multiprocessing import Pool
import numpy as np
import logging

def read_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(data):
    # Convert DataFrame to list of lists
    transactions = data.values.tolist()
    return transactions

def mine_association_rules(chunk):
    # Convert all values to strings
    chunk = [[str(item) for item in transaction] for transaction in chunk]

    # Use TransactionEncoder to transform the data into a one-hot encoded format
    te = TransactionEncoder()
    te_ary = te.fit_transform(chunk)
    df = pd.DataFrame(te_ary, columns=te.columns_)

    # Use FP-growth algorithm
    frequent_itemsets = fpgrowth(df, min_support=0.01, use_colnames=True)

    # Generate association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
    return rules

def save_rules(rules, output_path):
    rules.to_csv(output_path, index=False)

def rule_mining_main():
    data_path = "C:\\New folder\\aml-repo\\data_processed\\filtered_data_3.csv"
    output_path = "C:\\New folder\\aml-repo\\reports\\association_rules.csv"
    num_processes = 4  # Adjust the number of processes as needed
    chunk_size = 1000  # Define your desired chunk size

    # Read data
    logging.warning("Reading Filtered Data 3...")
    data = read_data(data_path)
    logging.warning("Read Filtered Data 3")

    # Preprocess data
    logging.warning("Preprocessing Data...")
    processed_data = preprocess_data(data)
    logging.warning("Data Preprocessing Done")

    chunks = [processed_data[i:i + chunk_size] for i in range(0, len(processed_data), chunk_size)]

    with Pool(num_processes) as pool:
        logging.warning(f"Starting Rule Mining with {num_processes} processes...")
        result_chunks = pool.map(mine_association_rules, chunks)

    rules = pd.concat(result_chunks, ignore_index=True)

    # Save rules
    logging.warning("Saving Rules...")
    save_rules(rules, output_path)
    logging.warning("Saving Rules Done")

if __name__ == "__main__":
    logging.basicConfig(filename='C:\\New folder\\aml-repo\\logs\\model_development.txt',
                        filemode='a',
                        format='%(asctime)s %(message)s',
                        datefmt="%Y-%m-%d %H:%M:%S")
    logging.warning("----------")
    logging.warning("RULE MINING STAGE")
    rule_mining_main()
    print("Rule mining run successfully")
