import streamlit as st  #type:ignore

st.set_page_config(page_title="Page à propos", page_icon="🌍") # titre affiché dans l'onglet
st.markdown('# <div style="text-align: center;"> <span style="color: blue;">Projet d’IA : Détection automatisée de la Tuberculose par Computer Vision</span> </div>', unsafe_allow_html=True)
st.sidebar.header("Description du projet")



st.markdown('# <span style="color: #800080;"> Introduction</span>', unsafe_allow_html=True)
st.write(
    """
    <div style="text-align: justify;">
    Les avancées en intelligence artificielle ont ouvert des horizons révolutionnaires dans le domaine de la médecine. Mon projet combine la Computer Vision à la puissance du Deep Learning pour résoudre un enjeu crucial : la détection précoce de la tuberculose, une maladie majeure de santé publique.

    La tuberculose reste un défi mondial, nécessitant un diagnostic précoce. Notre objectif est de créer un modèle d'Intelligence Artificielle capable de détecter la tuberculose à partir d'images médicales, comme les radiographies pulmonaires. Imaginez un modèle capable d'analyser rapidement et précisément ces images, en identifiant les signes de la maladie que même l'œil humain pourrait manquer. Cela pourrait révolutionner la manière dont nous diagnostiquons la tuberculose, en rendant le processus plus rapide, plus accessible et plus précis.

    Au cours de cette présentation, nous explorerons la méthodologie du projet, de la collecte de données à la détection de la tuberculose, en soulignant son importance pour la santé publique et ses futures implications.

    En résumé, ce projet unit la Computer Vision et le Deep Learning pour améliorer la détection de la tuberculose, contribuant ainsi à la lutte contre cette maladie dévastatrice.

    </div>
    """,unsafe_allow_html=True
)


st.markdown('# <span style="color: red;">A. Objectif du Projet', unsafe_allow_html=True)

st.write(
    """
    <div style="text-align: justify;">
    L'objectif principal de ce projet est de développer un modèle d'Intelligence Artificielle capable de détecter la tuberculose à partir d'images médicales, telles que les radiographies pulmonaires. La détection précoce de la tuberculose est essentielle pour un traitement efficace et la réduction de la propagation de la maladie.</div>""",unsafe_allow_html=True
)


st.markdown('# <span style="color: red;">B. Méthodologie :', unsafe_allow_html=True)
st.write(
    """
    <div style="text-align: justify;">

    1.  <b>Collecte de Données :</b> J'ai rassemblé une vaste collection d'images médicales, notamment des radiographies pulmonaires de patients atteints de tuberculose et de patients en bonne santé. Ces données serviront à l'entraînement et à la validation du modèle.

    2.  <b>Source des données :</b> https://www.kaggle.com/datasets/tolgadincer/labeled-chest-xray-images 

    3.  <b>Prétraitement des Données :</b> Les images ont été prétraitées pour éliminer le bruit, ajuster la résolution et normaliser les couleurs, afin de les préparer à l'analyse par l'IA.

    3.	<b>Architecture du Modèle :</b> J'ai conçu un modèle de Deep Learning basé sur des réseaux de neurones convolutionnels (CNN) pour extraire des caractéristiques pertinentes des images médicales.

    4.	<b>Entraînement et Validation :</b> Le modèle a été entraîné sur l'ensemble de données en utilisant des techniques de Deep Learning. J'ai utilisé une validation croisée pour évaluer la performance du modèle.

    5.	<b>Détection :</b> Une fois entraîné, le modèle est capable de détecter automatiquement la présence de tuberculose dans de nouvelles images médicales.

    """,unsafe_allow_html=True
)

st.markdown('# <span style="color: red;">C. Importance :', unsafe_allow_html=True)
st.write(
    """
    <div style="text-align: justify;">
    La détection automatisée de la tuberculose par Computer Vision avec le Deep Learning offre de nombreux avantages, notamment la rapidité, la précision et la possibilité d'assister les professionnels de la santé dans le diagnostic précoce de la maladie.
    """,unsafe_allow_html=True
)

st.markdown('# <span style="color: red;">D. Perspectives Futures :', unsafe_allow_html=True)
st.write(
    """
    <div style="text-align: justify;">
    Mon travail de recherche se poursuit avec l'exploration de méthodes avancées de Deep Learning pour améliorer encore la précision de la détection de la tuberculose. Je suis également ouvert à des collaborations avec des experts en médecine et des organismes de santé pour mettre en œuvre cette technologie dans un contexte clinique.  """,unsafe_allow_html=True
)


st.markdown('# <span style="color: #800080;"> Conclusion :', unsafe_allow_html=True)
st.write(
    """
    <div style="text-align: justify;">
    La détection de la tuberculose par Computer Vision avec Deep Learning est une initiative qui vise à utiliser les avancées de l'IA pour améliorer les soins de santé et la lutte contre cette maladie grave. Ce projet illustre mon engagement envers la recherche de solutions novatrices et à fort impact dans le domaine de l'IA et de la santé publique. """,unsafe_allow_html=True)


