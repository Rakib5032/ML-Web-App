🛡️ IoT Threat Shield - ML-Based Threat Mitigation System
An AI-powered web application for IoT security threat detection and mitigation using machine learning algorithms and blockchain technology.

🚀 Features
Real-time Threat Detection: Advanced ML algorithms analyze IoT system parameters
Interactive Web Interface: Modern, responsive UI with real-time feedback
Blockchain Integration: Secure transaction processing with multiple consensus mechanisms
Multi-layer Analysis: Device, Network, and Application layer security assessment
Comprehensive Reporting: Detailed analysis reports with actionable recommendations
REST API: Programmatic access to threat prediction capabilities
📋 Prerequisites
Python 3.8 or higher
pip (Python package installer)
Virtual environment (recommended)
🛠️ Installation
Clone the repository
bash
git clone <your-repo-url>
cd ml_web_app
Create a virtual environment
bash
python -m venv venv
Activate the virtual environment
On Windows:

bash
venv\Scripts\activate
On macOS/Linux:

bash
source venv/bin/activate
Install dependencies
bash
pip install -r requirements.txt
Place your trained models
Ensure random_forest_model.pkl is in the models/ directory
Ensure preprocessor.pkl is in the models/ directory
🚀 Running the Application
Start the Flask development server
bash
python app.py
Open your web browser and navigate to:
http://localhost:5000
📁 Project Structure
ml_web_app/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── models/                     # Saved ML models and preprocessors
│   ├── random_forest_model.pkl
│   └── preprocessor.pkl
├── templates/                  # HTML templates
│   ├── index.html               # Input form page
│   └── result.html              # Prediction output page
├── static/                     # Static assets
│   ├── style.css                # Custom styles
│   └── bootstrap.min.css        # Bootstrap CSS
└── README.md                   # Project documentation
🎯 How to Use
Web Interface
Navigate to the home page
Fill in the IoT system parameters:
Data Size (KB)
Processing Time (ms)
Attack Severity (0-10 scale)
Blockchain Transaction Time (ms)
Energy Consumption (mJ)
IoT Layer (Device/Network/Application)
Request Type
Security Threat Type
Consensus Mechanism
Click "Analyze Threat Level"
View the detailed results with:
Threat status (Mitigated/Detected)
Confidence percentage
Recommendations
Security best practices
REST API
Send POST requests to /api/predict with JSON data:

bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "data_size": 1024,
    "processing_time": 250,
    "attack_severity": 5,
    "blockchain_time": 500,
    "energy": 150,
    "iot_layer": "Device",
    "request_type": "Data Transmission",
    "threat_type": "Eavesdropping",
    "consensus": "PoA"
  }'
🔧 Configuration
Environment Variables
You can set the following environment variables:

FLASK_ENV: Set to development for development mode
FLASK_DEBUG: Set to 1 to enable debug mode
PORT: Port number for the application (default: 5000)
Model Files
The application expects the following files in the models/ directory:

random_forest_model.pkl: Trained Random Forest model
preprocessor.pkl: Data preprocessing pipeline
If these files are not found, the application will use a fallback prediction method.

📊 Input Parameters
Parameter	Type	Description	Range/Options
Data Size	Float	Size of data in KB	> 0
Processing Time	Float	Processing time in milliseconds	> 0
Attack Severity	Integer	Threat severity level	0-10
Blockchain Time	Float	Transaction time in milliseconds	> 0
Energy Consumption	Float	Energy usage in millijoules	> 0
IoT Layer	String	Target IoT layer	Device/Network/Application
Request Type	String	Type of request	Data Transmission, Encrypted Data Transfer, Smart Contract Execution, Authentication
Security Threat	String	Type of threat	Eavesdropping, Man-in-the-Middle, Tampering, Unauthorized Access, DDoS
Consensus Mechanism	String	Blockchain consensus	PoA, PoS, PoW, PBFT
🎨 Features Overview
🎯 Threat Assessment
Real-time analysis of IoT security parameters
ML-based threat prediction with confidence scores
Multi-factor security evaluation
🔒 Security Levels
Low Risk (0-2): Minimal threat detected
Medium Risk (3-5): Moderate attention needed
High Risk (6-8): Immediate action required
Critical Risk (9-10): Emergency response needed
📱 Modern UI Features
Responsive design for all devices
Interactive range sliders
Real-time form validation
Animated feedback and transitions
Downloadable reports
Social sharing capabilities
🛡️ Security Best Practices
Regular firmware updates
Strong authentication protocols
Network segmentation
Continuous monitoring
End-to-end encryption
🔄 Development
Adding New Features
Backend: Modify app.py for new endpoints
Frontend: Update templates in templates/
Styling: Modify static/style.css
Model Updates
To update the ML models:

Train your new model
Save as .pkl files using joblib
Replace files in the models/ directory
Restart the application
🚀 Production Deployment
For production deployment:

Set environment variables:
bash
export FLASK_ENV=production
export FLASK_DEBUG=0
Use a production WSGI server like Gunicorn:
bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
Configure reverse proxy (Nginx recommended)
🤝 Contributing
Fork the repository
Create a feature branch
Make your changes
Add tests if applicable
Submit a pull request
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🆘 Support
For support, please:

Check the documentation
Review existing issues
Create a new issue with detailed information
🔮 Future Enhancements
 Real-time monitoring dashboard
 Advanced ML model ensemble
 Integration with IoT device APIs
 Historical threat analytics
 Advanced user authentication
 Multi-tenant support
 Docker containerization
 Cloud deployment templates
Made with ❤️ for IoT Security

