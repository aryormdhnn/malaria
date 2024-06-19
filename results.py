import streamlit as st

def show_results():
    st.markdown("<h1 style='text-align: center; color: white;'>Hasil Pemeriksaan</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style='text-align: center; color: grey;'>
        Ini adalah bagian hasil pemeriksaan dari aplikasi Malaria Detection. Di sini, Anda dapat melihat riwayat pemeriksaan yang telah dilakukan.
        </p>
        """,
        unsafe_allow_html=True
    )

    if 'results' in st.session_state and st.session_state['results']:
        st.table(st.session_state['results'])
    else:
        st.markdown("<p style='text-align: center; color: grey;'>Belum ada hasil pemeriksaan.</p>", unsafe_allow_html=True)
