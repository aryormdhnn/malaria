import streamlit as st

def login():
    # Periksa apakah pengguna sudah autentikasi
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if st.session_state["authenticated"]:
        st.write("You are already logged in.")
        return
    
    st.markdown(
        """
        <style>
        .main {
            background-color: #0e1117;
            color: white;
        }
        .login-container {
            max-width: 400px;
            margin: auto;
            padding: 2rem;
            border-radius: 10px;
            background-color: #1e2228;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .login-container h2 {
            text-align: center;
            margin-bottom: 2rem;
            color: #0097ff;
        }
        .login-container input {
            width: 100%;
            padding: 1rem;
            margin: 0.5rem 0;
            border-radius: 5px;
            border: none;
            background-color: #333;
            color: white;
        }
        .login-container button {
            width: 100%;
            padding: 1rem;
            border: none;
            border-radius: 5px;
            background-color: #3380CC;
            color: white;
            font-size: 1rem;
            cursor: pointer;
        }
        .login-container button:hover {
            background-color: #18e73e;
        }
        </style>
       
        """
    , unsafe_allow_html=True)

    st.markdown("<h2>Login</h2>", unsafe_allow_html=True)

    username = st.text_input("", placeholder="Username")
    password = st.text_input("", type="password", placeholder="Password")

    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state["authenticated"] = True
            st.success("Login successful")
            st.experimental_rerun()  # Muat ulang halaman setelah login
        else:
            st.error("Invalid username or password")

    st.markdown("</div>", unsafe_allow_html=True)

def logout():
    st.session_state["authenticated"] = False
    st.success("Logged out successfully")
    st.experimental_rerun()  # Muat ulang halaman setelah logout
