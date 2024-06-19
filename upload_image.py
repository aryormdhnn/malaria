import os
import gdown
import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

def download_model(file_id, output_path):
    try:
        if not os.path.exists(output_path):
            url = f'https://drive.google.com/uc?id={file_id}'
            gdown.download(url, output_path, quiet=True)
    except Exception as e:
        return f"Error downloading the model: {e}"
    return None

def preprocess_image(img, target_size):
    img = img.resize(target_size)
    array = image.img_to_array(img)
    array = np.expand_dims(array, axis=0)
    array = array / 255.0  # Normalisasi
    return array

def is_valid_image(img):
    return img.mode == 'RGB'

def load_malaria_model(model_path):
    return load_model(model_path)

def show_upload_image(model):
    st.markdown("<h1 style='text-align: center; color: white;'>Aplikasi Deteksi Malaria</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: grey;'>Unggah gambar untuk mendeteksi malaria. Ukuran file maksimum adalah 100 KB.</p>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Unggah gambar untuk mendeteksi malaria. Ukuran file maksimum adalah 100 KB.", type=["png", "jpg", "jpeg", "bmp"], help="Limit 100KB per file • PNG, JPG, JPEG, BMP")

    if uploaded_file is not None:
        # Check file size
        file_size = uploaded_file.size
        if file_size > 100 * 1024:  # 100 KB limit
            st.warning("Gambar yang diunggah terlalu besar. Silakan unggah gambar yang lebih kecil dari 100 KB.")
        else:
            img = Image.open(uploaded_file)
            
            if not is_valid_image(img):
                st.warning("Gambar yang diunggah tidak sesuai dengan karakteristik yang diharapkan dari dataset. Silakan unggah gambar berwarna (RGB).")
            else:
                img_array = preprocess_image(img, target_size=(128, 128))
                
                with st.spinner('Mengklasifikasikan...'):
                    prediction = model.predict(img_array)
                    malaria_probability = prediction[0][0] * 100
                    result = 'Malaria' if malaria_probability > 50 else 'Bukan Malaria'
                
                st.image(img, caption='Unggah Gambar', use_column_width=True)
                st.markdown(f"<h3 style='text-align: center; color: white;'>Prediksi: {result}</h3>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align: center; color: grey;'>Kemungkinan Malaria: {malaria_probability:.2f}%</p>", unsafe_allow_html=True)
                
                st.progress(malaria_probability / 100)
                
                # Save results in session
                if 'results' not in st.session_state:
                    st.session_state['results'] = []
                st.session_state['results'].append({
                    "Image": uploaded_file.name,
                    "Prediction": result,
                    "Probability": f"{malaria_probability:.2f}%"
                })

# Main script
model_file_id = '17-dxaC04oO95hMExUC_IOoPO0RaRlfkF'  # Replace with your Google Drive file ID
model_path = 'Nadam_TTS_Epoch50.h5'  # Path where the model will be saved

download_error = download_model(model_file_id, model_path)
if download_error:
    st.error(download_error)
else:
    model = load_malaria_model(model_path)
    show_upload_image(model)
