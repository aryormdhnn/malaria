import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from PIL import Image
import gdown
import os

# Function to download the model from Google Drive
def download_model(file_id, output_path):
    try:
        if not os.path.exists(output_path):
            url = f'https://drive.google.com/uc?id={file_id}'
            gdown.download(url, output_path, quiet=True)
    except Exception as e:
        st.error(f"Error downloading the model: {e}")

# Download model if it does not exist locally
file_id = '17-dxaC04oO95hMExUC_IOoPO0RaRlfkF'
model_path = 'Nadam_TTS_Epoch50.h5'
download_model(file_id, model_path)

# Load the model
model = load_model(model_path)

def preprocess_image(img, size):
    img = img.resize(size)
    array = image.img_to_array(img)
    array = np.expand_dims(array, axis=0)
    return array

# Add custom CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border: None;
        border-radius: 5px;
        padding: 10px;
    }
    .stFileUploader>button {
        background-color: #1f77b4;
        color: white;
        border: None;
        border-radius: 5px;
        padding: 10px;
    }
    .stProgress>div>div {
        background-color: #1f77b4;
    }
    .stTextInput>div>div>input {
        color: black;
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar menu
menu = st.sidebar.radio(
    "Menu",
    ("Home", "Upload Image", "About")
)

# Home section
if menu == "Home":
    st.markdown("<h1 style='text-align: center; color: white;'>Malaria Detection App</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: grey;'>Welcome to the Malaria Detection App. Use the menu to navigate through the app.</p>", unsafe_allow_html=True)

# Upload Image section
elif menu == "Upload Image":
    st.markdown("<h1 style='text-align: center; color: white;'>Malaria Detection App</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: grey;'>Upload an image to detect malaria.</p>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg", "bmp"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        img = img.resize((256, 256))  # Resize uploaded image
        img_array = preprocess_image(img, size=(128, 128))
        
        with st.spinner('Classifying...'):
            prediction = model.predict(img_array)
            malaria_probability = prediction[0][0] * 100
            result = 'Malaria' if malaria_probability > 50 else 'No Malaria'
        
        st.image(img, caption='Uploaded Image', use_column_width=True, channels="RGB")
        st.markdown(f"<h3 style='text-align: center; color: white;'>Prediction: {result}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: grey;'>Probability: {malaria_probability:.2f}%</p>", unsafe_allow_html=True)
        
        # Confidence score bar
        st.progress(malaria_probability / 100)

# About section
elif menu == "About":
    st.markdown("<h1 style='text-align: center; color: white;'>About This App</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style='text-align: center; color: grey;'>
        This Malaria Detection App uses a trained neural network model to predict the presence of malaria in blood smear images.
        Simply upload an image of a blood smear, and the app will analyze it and provide a prediction.
        </p>
        <p style='text-align: center; color: grey;'>
        The model was trained using a dataset of blood smear images, and the accuracy is quite high.
        However, please note that this app is for educational purposes only and should not be used for medical diagnosis.
        </p>
        """,
        unsafe_allow_html=True
    )

# Custom footer
st.markdown("<p style='text-align: center; color: grey;'>© 2024 Malaria Detection App</p>", unsafe_allow_html=True)
