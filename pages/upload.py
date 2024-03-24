import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.applications import InceptionV3
import numpy as np
import cv2
import streamlit as st
import os
import io

class ImagePredictor:
    def __init__(self, model_path):
        self.model = self.load_model(model_path)

    def preprocess_image(self, image):
        file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
        # Decode image
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        resized_image = cv2.resize(img, (300, 300))
        # You may add more preprocessing steps here if required
        return resized_image

    def load_model(self, model_path):
        base_model = InceptionV3(weights='imagenet', include_top=False, input_tensor=Input(shape=(300, 300, 3)))
        for layer in base_model.layers:
            layer.trainable = True
        x = tf.keras.layers.GlobalAveragePooling2D()(base_model.output)
        x = Dense(2056, activation='relu')(x)
        x = Dropout(0.3)(x)
        x = Dense(32, activation='relu')(x)
        x = Dropout(0.3)(x)
        output = Dense(1, activation='sigmoid')(x)
        #model device to use cpu/ gpu
        model = Model(inputs=base_model.input, outputs=output)
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        model.load_weights(model_path)
        if model is None:
            raise ValueError("Model not found")
        tf.device('/device:/cpu:0')
        return model

    def predict(self, image_array):
        predictions = []
        for image in image_array:
            preprocessed_image = self.preprocess_image(image)
            prediction = self.model.predict(np.expand_dims(preprocessed_image, axis=0))
            predictions.append(prediction)
            mean_prediction = np.mean(predictions)
            if mean_prediction < 0.5:
                return "The X-ray image is abnormal"
            else:
                return "The X-ray image is normal"
st.set_page_config(page_title="X-ray Analyzer", page_icon="./app/static/logo.jpg", layout="wide", menu_items={
    })
st.write('<style>div.block-container{padding-top:0.5rem;}</style>', unsafe_allow_html=True)
with open("static/base.html") as f:
    st.markdown(f.read(), unsafe_allow_html=True)
st.markdown(
        """
        <style>
        .st-emotion-cache-10trblm.e1nzilvr1 {
            font-family: "Black Han Sans", sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.title("Upload an X-ray image to be analyzed")
path = "pages/model_final.h5" 
predictor = ImagePredictor(path)

def example_image_loader():
    image_paths = ['static/image1.png', 'static/image2.png', 'static/image3.png']
    uploaded_files = []
    for image_path in image_paths:
        with open(image_path, 'rb') as file:
            uploaded_files.append(io.BytesIO(file.read()))
    return uploaded_files
    

if st.button("Load example images"):
    uploaded_files = example_image_loader()
    prediction = predictor.predict(uploaded_files)
    if prediction == "The X-ray image is abnormal":
        st.error(prediction)
    else:
        st.success(prediction)
    num_images = len(uploaded_files)
    num_columns = 4
    num_rows = -(-num_images // num_columns)
    for i in range(num_rows):
        cols = st.columns(num_columns)
        for j in range(num_columns):
            index = i * num_columns + j
            if index < num_images:
                cols[j].image(uploaded_files[index], width=300, caption="Uploaded X-ray image")



uploaded_files = st.file_uploader("You can upload your xray", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
if uploaded_files is None:
    st.info("Please upload an X-ray image")
elif uploaded_files is not None:
    prediction = predictor.predict(uploaded_files)
    if prediction == "The X-ray image is abnormal":
        st.error(prediction)
    elif prediction == "The X-ray image is normal":
        st.success(prediction)
    else:
        st.info("Please upload an X-ray image")
    num_images = len(uploaded_files)
    num_columns = 4
    num_rows = -(-num_images // num_columns)
    for i in range(num_rows):
        cols = st.columns(num_columns)
        for j in range(num_columns):
            index = i * num_columns + j
            if index < num_images:
                cols[j].image(uploaded_files[index], width=300, caption="Uploaded X-ray image")