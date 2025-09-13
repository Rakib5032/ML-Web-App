from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import joblib

# Load pre-trained model and preprocessor
model = joblib.load('models/random_forest_model.pkl')
preprocessor = joblib.load('models/preprocessor.pkl')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Collect user input
        data = {
            'Data Size (KB)': [float(request.form['data_size'])],
            'Processing Time (ms)': [float(request.form['processing_time'])],
            'Attack Severity (0-10)': [float(request.form['attack_severity'])],
            'Blockchain Transaction Time (ms)': [float(request.form['blockchain_time'])],
            'Energy Consumption (mJ)': [float(request.form['energy'])],
            'IoT Layer': [request.form['iot_layer']],
            'Request Type': [request.form['request_type']],
            'Security Threat Type': [request.form['threat_type']],
            'Consensus Mechanism': [request.form['consensus']]
        }

        df = pd.DataFrame(data)
        X_processed = preprocessor.transform(df)
        prediction = model.predict(X_processed)[0]

        # Decide warning based on prediction
        if prediction == 0:
            status = "Threat Not Mitigated"
            warning = "⚠️ Risk Detected! Immediate attention required."
        else:
            status = "Threat Mitigated"
            warning = "✅ System Safe."

        # Redirect to result page
        return render_template('result.html', status=status, warning=warning)

    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)
