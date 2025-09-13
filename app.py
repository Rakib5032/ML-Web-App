from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load model and preprocessor
try:
    model = joblib.load('models/random_forest_model.pkl')
    preprocessor = joblib.load('models/preprocessor.pkl')
    print("Models loaded successfully!")
except FileNotFoundError:
    print("Warning: Model files not found. Please ensure models are in the 'models' directory.")
    model = None
    preprocessor = None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            # Collect input data
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

            # Create DataFrame and make prediction
            df = pd.DataFrame(data)
            
            if model and preprocessor:
                X_processed = preprocessor.transform(df)
                prediction = model.predict(X_processed)[0]
                probability = model.predict_proba(X_processed)[0]
                confidence = max(probability) * 100
            else:
                # Fallback for demo purposes when models aren't available
                prediction = 1 if float(request.form['attack_severity']) <= 5 else 0
                confidence = 85.5

            # Determine status message and styling
            if prediction == 1:
                status = "Threat Mitigated"
                status_class = "success"
                icon = "✅"
                message = "Your IoT system is secure. No immediate threats detected."
                recommendation = "Continue monitoring your system with regular security assessments."
            else:
                status = "Threat Detected"
                status_class = "danger"
                icon = "⚠️"
                message = "Security vulnerability identified. Immediate action recommended."
                recommendation = "Implement additional security measures and review your system configuration."

            # Pass data to result template
            result_data = {
                'status': status,
                'status_class': status_class,
                'icon': icon,
                'message': message,
                'recommendation': recommendation,
                'confidence': round(confidence, 1),
                'input_data': data
            }

            return render_template('result.html', **result_data)

        except Exception as e:
            error_msg = f"An error occurred during prediction: {str(e)}"
            return render_template('index.html', error=error_msg)

    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for predictions"""
    try:
        data = request.get_json()
        
        # Convert to DataFrame format expected by model
        df_data = {
            'Data Size (KB)': [float(data['data_size'])],
            'Processing Time (ms)': [float(data['processing_time'])],
            'Attack Severity (0-10)': [float(data['attack_severity'])],
            'Blockchain Transaction Time (ms)': [float(data['blockchain_time'])],
            'Energy Consumption (mJ)': [float(data['energy'])],
            'IoT Layer': [data['iot_layer']],
            'Request Type': [data['request_type']],
            'Security Threat Type': [data['threat_type']],
            'Consensus Mechanism': [data['consensus']]
        }
        
        df = pd.DataFrame(df_data)
        
        if model and preprocessor:
            X_processed = preprocessor.transform(df)
            prediction = model.predict(X_processed)[0]
            probability = model.predict_proba(X_processed)[0]
            confidence = max(probability) * 100
        else:
            prediction = 1 if float(data['attack_severity']) <= 5 else 0
            confidence = 85.5
            
        return jsonify({
            'success': True,
            'prediction': int(prediction),
            'confidence': round(confidence, 1),
            'status': 'Threat Mitigated' if prediction == 1 else 'Threat Detected'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    # Create necessary directories if they don't exist
    
    app.run(debug=True, host='0.0.0.0', port=5000)