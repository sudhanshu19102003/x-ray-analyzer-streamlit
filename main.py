import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="X-ray Analyzer", page_icon="./app/static/logo.jpg", layout="wide", menu_items={
    })
st.write('<style>div.block-container{padding-top:0.5rem;}</style>', unsafe_allow_html=True)

with open("static/base.html") as f:
    st.markdown(f.read(), unsafe_allow_html=True)
#center the title of the page
st.markdown("""<h1 style='text-align: center;
            font-family: "Black Han Sans", sans-serif;
            margin-top: 10px;'>Welcome to X-ray Image Analysis</h1>""", unsafe_allow_html=True)
st.markdown("""
<style>
        /* Add your custom CSS styles here */
        .description {
            background-color: #404040;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(1, 1, 1, 0.1);
            font-family: Arial, sans-serif;
        }

        .description p {
            color: #fff;
            font-family: "Black Han Sans", sans-serif;
            font-size: 16px;
            line-height: 1.6;
            margin: 10px 0;
        }
    </style>
<div class="description">
    <h2>About Us</h2>
    <p>Welcome to our X-ray diagnostic services! We specialize in providing accurate and reliable X-ray imaging for diagnosing various medical conditions. Our state-of-the-art facilities and experienced radiologists ensure that you receive high-quality diagnostic results.</p>
    <p>Whether you're seeking routine screenings or specific diagnostic procedures, we are here to cater to your needs. Our advanced imaging technology allows us to capture detailed images, aiding in the identification and treatment of health issues.</p>
    <p>At X-ray Diagnostic, patient care and comfort are our top priorities. We strive to create a welcoming environment and ensure that your experience with us is as smooth and stress-free as possible.</p>
    <p>Explore our website to learn more about our services, staff, and facilities. If you have any questions or would like to schedule an appointment, feel free to contact us. We look forward to assisting you with your diagnostic needs.</p>
    <br>
    <a target="_self" href="/upload">
      <button style="background-color: #4CAF50;
            font-family: 'Black Han Sans', sans-serif;
            font-size: 21px;
            border-radius: 10px">
            try it out now >
      </button>
    </a>
</div>
""", unsafe_allow_html=True)


    


