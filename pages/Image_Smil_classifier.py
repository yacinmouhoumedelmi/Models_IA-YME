import pathlib
import streamlit as st
import numpy as np
from utils import smil_prediction, TB_prediction, show_code  # type:ignore

root_folder = pathlib.Path(__file__).parent.parent.resolve()  # current directory

st.set_page_config(page_title="Smilling prediction page")  # titre affiché dans l'onglet
st.sidebar.header("Prediction page for Smil and no smil")  # titre affiché dans la marge

st.markdown('# <div style="text-align: center;"> <span style="color: red;">Modèle de prédiction automatique pour le sourire et absence de sourire</span> </div>', unsafe_allow_html=True)  # titre affiché dans la page


st.write(
    """
    This page displays a form.\n
    Upload an image inside the form.\n
    Please press submit to make a prediction
"""
)

# https://docs.streamlit.io/library/api-reference/control-flow/st.form

with st.form("my_form"):
    # affichage formulaire
    uploaded_file = st.file_uploader("Choose a jpeg file containing humain face: ")
    submitted = st.form_submit_button(label="Submit")

    # is le bouton submit a été cliqué, il recevra la valeur vraie
    if submitted:
        if uploaded_file is not None:
            # where I want to save the file
            saved_file_path = root_folder / "uploads" / uploaded_file.name
            # save uploaded file somewhere
            with open(saved_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # display the uploaded image
            st.image(uploaded_file.getvalue())

            # make prediction and display prediction
            prediction = smil_prediction(saved_file_path)
            st.write(f"With the picture you submitted, the prediction is: {prediction}")

