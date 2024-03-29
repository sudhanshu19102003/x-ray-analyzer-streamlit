import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.applications import InceptionV3
import cv2
import numpy as np

class ImagePredictor:
    def __init__(self):
        self.path = "pages/inc.h5"
        self.model = self.load_model(self.path)
        self.device = '/device:GPU:0' if tf.test.is_gpu_available() else '/device:CPU:0'

    def preprocess_image(self, image):
        file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        resized_image = cv2.resize(img, (300, 300))
        resized_image = resized_image / 255.0
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
        model = Model(inputs=base_model.input, outputs=output)
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        model.load_weights(model_path)
        if model is None:
            raise ValueError("Model not found")
        return model

    def predict(self, image_array, batch_size=32):
        predictions = []
        with tf.device(self.device):
            for i in range(0, len(image_array), batch_size):
                batch_images = [self.preprocess_image(image) for image in image_array[i:i+batch_size]]
                batch_predictions = self.model.predict(np.array(batch_images))
                predictions.extend(batch_predictions)
        mean_prediction = np.mean(predictions)
        if mean_prediction > 0.5:
            return "The X-ray images are abnormal"
        elif mean_prediction < 0.5:
            return "The X-ray images are normal"

