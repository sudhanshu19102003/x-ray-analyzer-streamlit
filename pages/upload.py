import streamlit as st
import io
from pages.model import ImagePredictor

@st.cache_resource(experimental_allow_widgets=True)
def load_model():
    predictor = ImagePredictor()
    return predictor

def set_page_configuration():
    st.set_page_config(
        page_title="X-ray Analyzer",
        page_icon="./app/static/logo.jpg",
        layout="wide",
        menu_items={}
    )
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

@st.cache_resource()
def example_image_loader():
    image_paths = ['static/image1.png', 'static/image2.png', 'static/image3.png']
    uploaded_files = []
    for image_path in image_paths:
        with open(image_path, 'rb') as file:
            uploaded_files.append(io.BytesIO(file.read()))
    return uploaded_files

def load_example_images():
    if st.button("Load example images"):
        uploaded_files = example_image_loader()
        predictor= load_model()
        prediction = predictor.predict(uploaded_files)
        process_xray_images(uploaded_files, prediction)
    else:
        st.info("Click the button to load example images")

def analyze_uploaded_images():
    uploaded_files = st.file_uploader("You can upload your xray", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    if uploaded_files is not None:
        predictor = load_model()
        prediction = predictor.predict(uploaded_files)
        process_xray_images(uploaded_files, prediction)

def process_xray_images(uploaded_files, prediction):
    if prediction == "The X-ray images are abnormal":
        st.error(prediction)
    elif prediction == "The X-ray images are normal":
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
                
def run_xray_upload():
    set_page_configuration()
    analyze_uploaded_images()
    load_example_images()


if __name__ == "__main__":
    run_xray_upload()
