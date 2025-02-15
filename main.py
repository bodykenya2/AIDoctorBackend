from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# A simple GET route for testing
@app.route('/')
def index():
    return "Hello! The Flask API is running."

# Disclaimer to include in every response
DISCLAIMER = (
    "Disclaimer: This information is for educational purposes only and should not be considered "
    "as medical advice. Please consult a licensed healthcare professional for any medical concerns."
)

# POST route for processing symptom data
@app.route('/api/medical-info', methods=['POST'])
def medical_info():
    data = request.get_json(force=True)
    symptoms = data.get('symptoms', '').lower()

    # Check for emergency symptoms
    emergency_keywords = ['chest pain', 'shortness of breath', 'severe bleeding', 'loss of consciousness']
    if any(keyword in symptoms for keyword in emergency_keywords):
        return jsonify({
            "response": (
                "Your symptoms may indicate a medical emergency. Please call your local emergency services immediately. " 
                + DISCLAIMER
            )
        })

    # General informational response
    response_message = (
        f"Based on your symptoms ('{symptoms}'), please note that this is not a diagnosis. "
        "It is recommended to consult a doctor for a proper evaluation. " + DISCLAIMER
    )
    return jsonify({"response": response_message})

if __name__ == '__main__':
    # Use the PORT environment variable if available (for deployment)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
  
