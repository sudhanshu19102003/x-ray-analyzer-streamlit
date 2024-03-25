import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.applications import InceptionV3
import cv2
import numpy as np

class ImagePredictor:
    def __init__(self):
        self.path = "pages/model_final.h5"
        self.model = self.load_model(self.path)

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
        #auto select device
        if tf.test.is_gpu_available():
            model = tf.device('/device:/gpu:0')
        else:
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