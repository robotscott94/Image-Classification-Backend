from flask import Flask, request, jsonify
import numpy as np
import os
from keras.models import load_model
from keras.preprocessing import image
from google.cloud import storage

app = Flask(__name__)

# Set up the Google Cloud Storage client
storage_client = storage.Client.from_service_account_json('utopian-precept-383721-4faeabe1c883.json')

# Function to download and load the model
def get_model(bucket_name, model_file_path, local_file_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

    # Get your bucket
    bucket = storage_client.get_bucket(bucket_name)

    # Download your model file
    blob = bucket.blob(model_file_path)
    blob.download_to_filename(local_file_path)

    # Load and return the model
    return load_model(local_file_path)

# Load the model
model = get_model('image_class_0530', 'ModernVTraditional.h5', 'models/ModernVTraditional.h5')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Save the file
        f = request.files['file']
        upload_dir = 'uploads'
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        filepath = os.path.join(upload_dir, f.filename)
        f.save(filepath)

        # Load and preprocess the image
        img = image.load_img(filepath, target_size=(150, 150)) 
        x = image.img_to_array(img) / 255.0  # assuming you normalized images during training
        x = np.expand_dims(x, axis=0)

        # Classify the image
        classes = model.predict(x)
        result = "new" if classes[0][0] > 0.5 else "old" 

        return jsonify(result=result)

    return '''
    <!doctype html>
    <title>Upload an image</title>
    <h1>Upload an image</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
