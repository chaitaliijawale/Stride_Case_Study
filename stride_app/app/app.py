from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from app.data_preprocessing import perform_data_preprocessing
from app.machine_learning import run_machine_learning

app = Flask(__name__)

# Set the path where uploaded CSV files will be stored
app.config['UPLOAD_FOLDER'] = 'uploads/'

# List of classification models
models = ['Naive Bayes', 'Logistic Regression', 'K-Nearest Neighbours', 'Support Vector Machine', 'Decision Tree', 'Random Forest', 'XGBOOST']

# Placeholder to store the processed data
processed_data = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    if request.method == 'POST':
        csv_file = request.files['csv_file']
        if csv_file:
            # Save the uploaded file to the UPLOAD_FOLDER
            file_path = app.config['UPLOAD_FOLDER'] + csv_file.filename
            csv_file.save(file_path)

            # Read the CSV file and preprocess the data
            global processed_data
            processed_data = perform_data_preprocessing(file_path)

            return redirect(url_for('dashboard'))

    # Redirect back to the index if no file is uploaded or there's an error
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if processed_data is None:
        # Redirect back to the index if no data is processed
        return redirect(url_for('index'))

    # Perform ML modeling and get model accuracies
    accuracies = {}
    for model_name in models:
        accuracy = run_machine_learning(model_name, processed_data, selected_features, target)
        accuracies[model_name] = accuracy

    return render_template('dashboard.html', accuracies=accuracies)

if __name__ == '__main__':
    # Set the selected features and target column
    selected_features = ['Interaction_Weight_Discount', 'Customer_Satisfaction_Score_encoded', 'Interaction_CustomerRating_Discount', 'Discount_offered', 'Weight_category_encoded', 'Weight_in_gms', 'Delivery_Time_per_Weight_encoded', 'Shipping_speed_encoded', 'Discount_category_encoded']
    target = 'Reached.on.Time_Y.N'

    app.run(debug=True)
