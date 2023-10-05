# étant donné que le modèle est au format pickle
# j'aurais besoin de tableau numpy pour les passer à mon modèle
import numpy as np
import streamlit as st
import inspect
from keras.models import load_model  # type: ignore
import tensorflow as tf  # type:ignore


# cette fonction attend 2 paramètres
# un chemin vers une image et un chemin vers un modèle de ML/DL
def smil_prediction(img, mdl="Image_Smil_classifier.h5"):
    # je précharge mon modèle
    model = load_model(mdl)

    # config pour annoncer la taille de mon image
    image_size = (256, 256)

    # demander à keras de récupérer l'image que je lui donne en paramètre
    loaded_image = tf.keras.utils.load_img(img, target_size=image_size)
    # et transformer cette image sous forme de tableau
    img_array = tf.keras.preprocessing.image.img_to_array(loaded_image)
    # expand_dims ????
    img_array = tf.expand_dims(img_array/255, 0)

    # j'effectue une prédiction
    # je donne l'image à mon modèle
    # et ce dernier va me renvoyer la prédiction
    predictions = model.predict(img_array)

    score = predictions[0][0]
    rslts1 = (
        f"This image is {(score)*100} percent no smil and {(1 - score)*100} percent smil."
    )
    # rslts = (score*100, (1 - score)*100)
    return rslts1

# cette fonction attend 2 paramètres
# un chemin vers une image et un chemin vers un modèle de ML/DL
def TB_prediction(img, mdl="Image_TB_classifier.h5"):
    # je précharge mon modèle
    model = load_model(mdl)

    # config pour annoncer la taille de mon image
    image_size = (256, 256)

    # demander à keras de récupérer l'image que je lui donne en paramètre
    loaded_image = tf.keras.utils.load_img(img, target_size=image_size)
    # et transformer cette image sous forme de tableau
    img_array = tf.keras.preprocessing.image.img_to_array(loaded_image)
    # expand_dims ????
    img_array = tf.expand_dims(img_array/255, 0)

    # j'effectue une prédiction
    # je donne l'image à mon modèle
    # et ce dernier va me renvoyer la prédiction
    predictions = model.predict(img_array)

    score = predictions[0][0]
    rslts2 = (
        f"This image is {(score)*100} percent normal and {(1 - score)*100} percent Tuberculosis."
    )
    # rslts = (score*100, (1 - score)*100)
    return rslts2


def show_code(demo):
    """Showing the code of the demo."""
    show_code = st.sidebar.checkbox("Show code", True)
    if show_code:
        # Showing the code of the demo.
        st.markdown("## Code ayant permis de faire la prédiction")
        # get all the lines of the function
        sourcelines, _ = inspect.getsourcelines(demo)
        # show the lines of code
        st.code(("".join(sourcelines)))
