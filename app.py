from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

#Load the trained model

with open('models/iris_model.pkl', 'rb') as f:
    model = pickle.load(f)

#species mapping
species_names = ['setosa', 'versicolor', 'virginica']

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        #extract features

        features = [
            data['sepal_length'],
            data['sepal_width'],
            data['petal_length'],
            data['petal_width']
        ]

        #make the prediction
        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0]

        return jsonify({
            "species": species_names[prediction],
            "confidence": float(max(probability)),
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)

