IoT Threat Mitigation Prediction Web App

This is a Flask-based web application that predicts whether a threat in an IoT environment will be mitigated or not based on user input. It uses a trained Random Forest model and pre-processing pipeline.

Folder Structure
ml_web_app/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── models/                     # Saved ML models and preprocessors
│   ├── random_forest_model.pkl
│   └── preprocessor.pkl
├── templates/                  # HTML templates
│   ├── index.html               # Input form page
│   └── result.html              # Prediction output page (optional)
├── static/                     # Static assets
│   ├── style.css                # Custom styles
│   └── bootstrap.min.css        # Bootstrap CSS
└── README.md                   # Project documentation

Features

Predicts whether a given IoT threat will be mitigated.

Handles numerical and categorical inputs.

Shows live value for slider inputs (e.g., Attack Severity).

Warns the user if a categorical input is not selected.

Form resets after submission to prevent cached data.


Create a virtual environment:

python -m venv venv


Activate the virtual environment:

Windows (PowerShell):

.\venv\Scripts\activate


Linux/Mac:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt

Usage

Run the Flask app locally:

python app.py


Open a web browser and go to:

http://127.0.0.1:5000


Fill out the form and submit to get the prediction.

How it Works

Pre-processing: Input data is pre-processed using the saved preprocessor.pkl.

Numerical features are scaled using StandardScaler.

Categorical features are one-hot encoded.

Model Prediction: The pre-processed data is fed to the random_forest_model.pkl to predict the output.

Output: Shows whether the threat is mitigated (1) or not (0). Optional warning messages can be displayed based on prediction.