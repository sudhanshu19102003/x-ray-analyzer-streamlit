import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def display_overall_metrics():
    st.header("Overall Metrics")    
    metrics = {
        "Accuracy": 84.36,
        "Precision": 90.32,
        "Recall": 76.63,
        "Specificity": 91.95,
        "F1 Score": 82.91,
        "Cohen's Kappa": 68.67
    } 

    # Define column layout
    col1, col2 = st.columns([2, 3])

    # Display metrics
    with col1:
        for metric, value in metrics.items():
            st.write(f"{metric}: {value}%")

    # Display image on the left side
    with col2:
        image = "static/Confusion.png"  # Replace with the actual path to your image
        st.image(image, caption='Confusion Matrix', width=350)

def discuss_dataset():
    st.header("Dataset")
    st.markdown("The dataset used for this project is the MURA (Musculoskeletal Radiographs) dataset.")
    st.markdown("MURA is a large dataset of musculoskeletal radiographs consisting of 40,561 studies from 14,863 patients, with a total of 58,775 multi-view radiographic images.")
    st.markdown("It is intended for use in developing machine learning algorithms to aid in the diagnosis of musculoskeletal pathologies.")

def showcase_model():
    st.header("Model")
    st.markdown("The model architecture used for this project is Inception V3, which is a convolutional neural network (CNN) architecture developed by Google.")
    st.markdown("Inception V3 is well-known for its performance in image classification tasks, with its ability to capture intricate patterns in images.")
    st.markdown("The model was trained on the MURA dataset to perform X-ray anomaly detection, specifically to identify musculoskeletal abnormalities in radiographic images.")
    st.markdown("The implementation was done using TensorFlow, a popular deep learning framework.")
    

def main():
    st.set_page_config(page_title="X-ray Analyzer", page_icon="./app/static/logo.jpg", layout="wide", menu_items={})
    st.write('<style>div.block-container{padding-top:0.5rem;}</style>', unsafe_allow_html=True)

    with open("static/base.html") as f:
        st.markdown(f.read(), unsafe_allow_html=True)

    st.title("X-ray Anomaly Detection System Documentation")
    display_overall_metrics()
    discuss_dataset()
    showcase_model()

if __name__ == "__main__":
    main()
