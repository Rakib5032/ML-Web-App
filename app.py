from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# ================================
# Load shared preprocessor
# ================================
try:
    preprocessor = joblib.load('models/preprocessor.pkl')
    print("Preprocessor loaded successfully!")
except FileNotFoundError:
    print("Warning: Preprocessor not found!")
    preprocessor = None

# ================================
# Load models (all share the same preprocessor)
# ================================
def load_model(path, name):
    try:
        model = joblib.load(path)
        print(f"{name} loaded successfully!")
    except FileNotFoundError:
        print(f"Warning: {name} not found at {path}")
        model = None
    return model

models = {
    'random_forest': {
        'model': load_model('models/random_forest_model.pkl', 'Random Forest'),
        'name': 'Random Forest'
    },
    'decision_tree': {
        'model': load_model('models/decision_tree_model.pkl', 'Decision Tree'),
        'name': 'Decision Tree'
    },
    'knn': {
        'model': load_model('models/knn_model.pkl', 'KNN'),
        'name': 'K-Nearest Neighbors'
    },
    'xgboost': {
        'model': load_model('models/xgboost_model.pkl', 'XGBoost'),
        'name': 'XGBoost'
    },
    'mlp': {
        'model': load_model('models/mlp_classifier_model.pkl', 'MLP'),
        'name': 'MLP Classifier'
    }
}


# ================================
# Flask routes
# ================================
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        try:
            selected_model = request.form.get('model_type', 'random_forest')
            if selected_model not in models:
                selected_model = 'random_forest'

            current_model = models[selected_model]['model']

            # Input data
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

            # Prediction
            if current_model:
                X_processed = preprocessor.transform(df) if preprocessor else df
                prediction = current_model.predict(X_processed)[0]
                probability = current_model.predict_proba(X_processed)[0] if hasattr(current_model, 'predict_proba') else [1.0, 0.0]
                confidence = max(probability) * 100
            else:
                # fallback demo
                prediction = 1 if float(request.form['attack_severity']) <= 5 else 0
                confidence = 85.5

            # Result
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

            return render_template('result.html', 
                                   status=status, status_class=status_class, icon=icon,
                                   message=message, recommendation=recommendation,
                                   confidence=round(confidence, 1), input_data=data,
                                   model_used=models[selected_model]['name'])

        except Exception as e:
            return render_template('index.html', error=str(e), models=models)

    return render_template('index.html', models=models)


@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.get_json()
        selected_model = data.get('model_type', 'random_forest')
        if selected_model not in models:
            selected_model = 'random_forest'

        current_model = models[selected_model]['model']

        df = pd.DataFrame({
            'Data Size (KB)': [float(data['data_size'])],
            'Processing Time (ms)': [float(data['processing_time'])],
            'Attack Severity (0-10)': [float(data['attack_severity'])],
            'Blockchain Transaction Time (ms)': [float(data['blockchain_time'])],
            'Energy Consumption (mJ)': [float(data['energy'])],
            'IoT Layer': [data['iot_layer']],
            'Request Type': [data['request_type']],
            'Security Threat Type': [data['threat_type']],
            'Consensus Mechanism': [data['consensus']]
        })

        if current_model:
            X_processed = preprocessor.transform(df) if preprocessor else df
            prediction = current_model.predict(X_processed)[0]
            probability = current_model.predict_proba(X_processed)[0] if hasattr(current_model, 'predict_proba') else [1.0, 0.0]
            confidence = max(probability) * 100
        else:
            prediction = 1 if float(data['attack_severity']) <= 5 else 0
            confidence = 85.5

        return jsonify({
            'success': True,
            'prediction': int(prediction),
            'confidence': round(confidence, 1),
            'status': 'Threat Mitigated' if prediction == 1 else 'Threat Detected',
            'model_used': models[selected_model]['name']
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

