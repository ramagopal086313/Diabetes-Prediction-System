"""This modules contains data about about page"""

# Import necessary modules
import streamlit as st
from PIL import Image


def app():
    """This function creates the about page"""
    st.balloons()
    st.title('Contact Us')
    st.markdown('''### Name:
    Krishnan Ramagopal''')
    st.image("./images/icon.jpg")
    st.markdown('''### GitHub: [Ramagopal](https://github.com/KrishnanRamagopal/)''')
    