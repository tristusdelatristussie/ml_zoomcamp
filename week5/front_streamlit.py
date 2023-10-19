import streamlit as st
import requests

# Fonction pour envoyer une requête POST au serveur Flask
def send_prediction_request(data):
    url = "http://localhost:9797/predict"  # Remplacez l'URL par celle de votre serveur Flask
    response = requests.post(url, json=data)
    return response.json()

# Interface utilisateur Streamlit
def main():
    st.title("Interface de prédiction")

    # Entrée utilisateur
    a = st.text_input("Entrez la profession")
    b = st.text_input("Durée")
    c = st.text_input("Resultat")

    if st.button("Prédire"):
        # Préparez les données pour la requête POST
        data = {"input_data": { "job": a, "duration" : b , "poutcome" : c}}

        # Envoyez la requête au serveur Flask
        response = send_prediction_request({ "job": a, "duration" : b , "poutcome" : c})

        # Affichez les résultats de la prédiction
       # st.write("Résultat de la prédiction:")


    with st.expander("Résultat"):
        st.write(response["prediction"][0][1])



if __name__ == "__main__":
    main()
