from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and preprocessor
model = joblib.load('models/random_forest_model.pkl')
preprocessor = joblib.load('models/preprocessor.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Collect input
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

        # Determine status message and color
        if prediction == 1:
            status = "Threat Mitigated"
            color = "success"
            warning = "No immediate risk detected."
        else:
            status = "Threat Detected"
            color = "danger"
            warning = "⚠️ Action required!"

        return render_template('result.html', status=status, color=color, warning=warning)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
