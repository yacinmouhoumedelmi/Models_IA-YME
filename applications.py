from PIL import Image
import streamlit as st



# entry point
def run():
    st.set_page_config(
        page_title="Home page",
        page_icon="👋",
    )
    

    # Ouvrir les deux images
    image1 = Image.open("logo.jpeg").resize((300, 200))
    image2 = Image.open("IA_photo.jpeg").resize((300, 200))
    image3 = Image.open("Djibouti.jpeg").resize((300, 200))

    # Récupérer les dimensions des images
    width, height = image1.size

    # Fusionner les images côte à côte

    new_image = Image.new("RGB", (width * 3, height))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (width, 0))
    new_image.paste(image3, (width * 2, 0))

    # Afficher l'image fusionnée dans Streamlit
    st.image(new_image, use_column_width=True)

    st.write(
    """
    # Bienvenu dans l'application web : \n
    # Modèles d'Intelligence Artificielle \n
    # conçus par M. Yacin MOUHOUMED
    """
    )
    

if __name__ == "__main__":
    run()
