import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import numpy as np
from tensorflow.keras.models import load_model
import cv2
import joblib

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
PREDICTION_FOLDER = 'static/predictions/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PREDICTION_FOLDER'] = PREDICTION_FOLDER

# Load your segmentation model
idx2rgb = joblib.load('Dict/idx2rgb.pkl')
model = load_model('model/unet.keras')

#Function to Decode predicted image
def map_class_to_rgb(p):
  return idx2rgb[p[0]]

def decoding_image(encoded_image):
    decoded_image = np.apply_along_axis(map_class_to_rgb, -1, np.expand_dims(np.argmax(encoded_image, axis=-1), -1))
    return decoded_image

# Function to predict the image
def predict_image(image_path):
    image_bgr = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    image_resized = cv2.resize(image_rgb, (256, 256))  # Adjust size based on model input
    image_array = np.expand_dims(image_resized, axis=0) / 255.0
    prediction = model.predict(image_array)
    decoded_prediction = decoding_image(prediction)
    prediction_squeezed = np.squeeze(decoded_prediction)
    if prediction_squeezed.dtype != 'uint8':
        prediction_squeezed = (prediction_squeezed * 255).astype('uint8')
    prediction_resized = cv2.resize(prediction_squeezed, (image_rgb.shape[1], image_rgb.shape[0]))
    return prediction_resized


# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')


# Route to upload an image
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'original_image': file_path})


# Route to predict image
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    image_path = data['image_path'].split('5000/')[1]
    prediction = predict_image(image_path)
    prediction_filename = 'prediction.png'
    prediction_path = os.path.join(app.config['PREDICTION_FOLDER'], prediction_filename)
    cv2.imwrite(prediction_path, prediction)

    return jsonify({'prediction_image': prediction_path})


# Route to clear images
@app.route('/clear', methods=['POST'])
def clear_images():
    for folder in [UPLOAD_FOLDER, PREDICTION_FOLDER]:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            os.remove(file_path)
    return jsonify({'message': 'Images cleared'})


# Route to save prediction
@app.route('/save', methods=['POST'])
def save_prediction():
    data = request.json
    prediction_image = data['prediction_image']
    save_path = os.path.join(app.config['PREDICTION_FOLDER'], 'saved_prediction.png')
    os.rename(prediction_image, save_path)
    return jsonify({'message': 'Prediction saved', 'save_path': save_path})


if __name__ == '__main__':
    app.run(debug=True)
