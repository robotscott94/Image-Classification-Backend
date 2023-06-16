# Image-Classification-Backend

This is the backend API service for an Image Classification Website, written in Python using Flask, Keras, and PIL.

## Description

This project is intended to serve as the backend for an image classification website. It receives images from the front-end, processes them using Keras and PIL, and then returns the predicted classifications. The predictions classify images as either "Modern" or "Traditional".

The main goal is to provide a reliable, fast, and accurate service for classifying images sent from the website frontend.

## Getting Started

### Dependencies

* Python 3.8 or higher
* Flask
* Flask-CORS
* Keras
* TensorFlow
* NumPy
* Pillow

You can install all dependencies by running the following command:

```console
pip install -r requirements.txt
```


### Installing and Running Locally

1. Clone the repository:
2. Install the necessary dependencies:
3. Before running the server locally, ensure you have the model file 'ModernVTraditional.h5' in the root directory of the project.
4. To start the server, run:
```console
python main.py
```

* In addition, the live URL, launched with the [Railway](Railway.app) can be viewed [here](image-api-production-87ba.up.railway.app).
