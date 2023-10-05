import streamlit as st  #type:ignore

st.set_page_config(page_title="Biographie", page_icon="🌍") # titre affiché dans l'onglet
st.markdown('# <div style="text-align: center;"> <span style="color: red;">Brève biographie</span> </div>', unsafe_allow_html=True)
st.sidebar.header("Présentation")

st.image('DemoDayYME.jpeg')

st.write(
    """
    <div style="text-align: justify;">
    <span style="color: blue;"><b> Yacin MOUHOUMED ELMI </b> </span> est <span style="color: red;"> <b>un doctorant en économétrie-statistique</b></span>, <span style="color: red;"><b>Data Scientist certifié</b></span>, et <span style="color: red;"><b>spécialiste en suivi-évaluation de projets</b> </span>. Depuis septembre 2023, il occupe le poste d'Assistant <span style="color: #800080;"><b>Sénior en suivi-évaluation et reporting</b></span> à l'OIM à Djibouti, où il utilise ses compétences analytiques, y compris les méthodes de machine Learning, de Deep Learning et de computer vision de l'Intelligence Artificielle (IA), pour éclairer les décisions stratégiques.

    Son engagement dans le domaine du suivi-évaluation comprend une formation récente en août 2023, couvrant des aspects clés tels que la création d'indicateurs et l'analyse des données. Il a également joué un rôle essentiel en tant que consultant national pour le PNUD en 2020, en contribuant à une enquête sur l'impact de la Covid-19 sur les ménages pauvres à Djibouti.

    En dehors de son travail, Yacin est passionné par la recherche scientifique et a publié un livre ainsi que deux articles, couvrant des sujets variés, de la Covid-19 à l'analyse des eaux minérales et à la modélisation économique de la France.

    En conclusion, <b>Yacin MOUHOUMED</b> est un professionnel dévoué à l'analyse des données, aux technique d'IA, et à la rédaction de rapports de suivi-évaluation pour orienter les décisions futures, croyant fermement en l'impact positif et durable de l'analyse des données.

    </div>
    """,unsafe_allow_html=True
)
