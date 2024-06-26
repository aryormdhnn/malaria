import streamlit as st

def show_home():
    st.markdown("""
        <style>
        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        </style>
        """, unsafe_allow_html=True)
    
    st.image("logo.png", width=200,
             
             )  # Mengatur lebar gambar menjadi 200 piksel
    st.markdown("<h1 style='text-align: center; color: white;'>Aplikasi Deteksi Malaria</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: grey;'>Selamat datang di Aplikasi Deteksi Malaria. Gunakan menu untuk menavigasi aplikasi.</p>", unsafe_allow_html=True)

# Contoh cara menjalankan halaman home
if __name__ == "__main__":
    show_home()
