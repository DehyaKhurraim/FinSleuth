from flask import Flask, request, render_template, redirect, url_for
import pickle
import subprocess
import mysql.connector
import time
headers = {"Authorization": "Bearer ya29.a0ARrdaM_YkI6oUm949UJteFylUpoLGG114jpBLlEiTSJZkfPSqwPaUcWmJKHRN9aPNBpOZoXdbCjC5BRezFaooZSVvfFqMyKkbmb_ZuuxrzkARnNJh06-Dm-xvq4FVlpmnoBm1IF2n4seBnhRjV79Si4XmNS7"}

model_path = 'saved_models/model.pkl'
model = pickle.load(open(model_path, 'rb'))

app = Flask(__name__)
execution_complete = False


# AML configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345',
    'database': 'FYP_AML'
}

# Establishing connection to the database
conn = mysql.connector.connect(**db_config)

# Creating the users table if it does not exist
try:
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    """)
    print("Users table created successfully.")
    conn.commit()
    cursor.close()
except mysql.connector.Error as e:
    print(f"An error occurred: {str(e)}")
    conn.rollback()

@app.route("/", methods=['GET'])
def signin_page():
    return render_template('signin.html')
    # return render_template('index.html')

@app.route("/login", methods=['POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    
        try:
            cursor = conn.cursor()
            select_query = "SELECT * FROM users WHERE email = %s"
            cursor.execute(select_query, (email,))
            user = cursor.fetchone()
            if user:
                if password == user[3]:
                    return redirect(url_for('index'))
                else:
                    return "Incorrect password. Please try again."
            else:
                return "User with this email does not exist. Please try again."
            
        except mysql.connector.Error as e:
            return f"An error occurred: {str(e)}"

    else:
        return redirect(url_for('signin_page'))

@app.route("/signuppage", methods=['GET'])
def signup_page():
    return render_template('signup.html')

@app.route("/signup", methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        try:
            cursor = conn.cursor()
            insert_query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (username, email, password))
            conn.commit()
            cursor.close()
            return redirect(url_for('signin_page'))

        except mysql.connector.Error as e:
            conn.rollback()
            return f"An error occurred: {str(e)}"

    else:
        return render_template('signup.html')

@app.route("/adddata", methods=['GET'])
def adddata():  
    return render_template('adddata.html')


@app.route("/index", methods=['GET'])
def index():
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM Suspicious"
        cursor.execute(query)
        suspicious_data = cursor.fetchall()
        return render_template('index.html', suspicious_data=suspicious_data)
    except mysql.connector.Error as e:
        return f"An error occurred: {str(e)}"

@app.route("/run_files", methods=['POST'])
def run_files():
    try:
        # List of file names to run
        file_names = [
            '/data_preprocessing_1.py',
            '/data_preprocessing_2.py',
            '/data_preprocessing_3.py',
            '/rule_mining.py',
            '/feature_selection.py',
             '/model_creation.py',
             '/dbconnection.py'
        ]
        
        # Path to the src directory
        src_directory = 'C:/New folder/aml-repo/src'

        # List to store executed file names
        executed_files = []

        # Loop through each file and execute it
        for file_name in file_names:
            file_path = src_directory + file_name
            subprocess.run(['python', file_path], check=True)
            executed_files.append(file_name)  # Append the executed file name
        
        # # Display a modal after the execution of all files
        # execution_complete = True
        # time.sleep(5)

        return render_template("adddata.html", name=executed_files)
    

    except Exception as e:
        return f"An error occurred: {str(e)}"
if __name__ == "__main__":
    app.run()