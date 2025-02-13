import streamlit as st
from tools import flsm_vlsm, port_scanner, packet_analyzer

def main():
    st.set_page_config(page_title="CyberToolbox", layout="wide")

    st.title("🔐 CyberToolbox - Outils de Cybersécurité")

    # Menu de navigation par catégories
    category = st.sidebar.selectbox("Sélectionnez une catégorie", ["Réseau", "BruteForce", "Forensics", "Outils Divers"])

    if category == "Réseau":
        tool = st.sidebar.selectbox("Choisissez un outil", ["FLSM/VLSM", "Analyse de paquets", "Scan de ports"])

        if tool == "FLSM/VLSM":
            flsm_vlsm.run()
        elif tool == "Analyse de paquets":
            packet_analyzer.run()
        elif tool == "Scan de ports":
            port_scanner.run()

    elif category == "BruteForce":
        tool = st.sidebar.selectbox("Choisissez un outil", ["Générateur de mots de passe", "Crackeur de hachage"])

        if tool == "Générateur de mots de passe":
            st.write("🔑 Fonctionnalité en cours de développement")
        elif tool == "Crackeur de hachage":
            st.write("🛠️ Fonctionnalité en cours de développement")

    elif category == "Forensics":
        tool = st.sidebar.selectbox("Choisissez un outil", ["Analyse de journaux", "Extraction de métadonnées"])

        if tool == "Analyse de journaux":
            st.write("📑 Fonctionnalité en cours de développement")
        elif tool == "Extraction de métadonnées":
            st.write("🔍 Fonctionnalité en cours de développement")

    elif category == "Outils Divers":
        tool = st.sidebar.selectbox("Choisissez un outil", ["Convertisseur d'encodage", "Calculateur de checksum"])

        if tool == "Convertisseur d'encodage":
            st.write("🔢 Fonctionnalité en cours de développement")
        elif tool == "Calculateur de checksum":
            st.write("🔍 Fonctionnalité en cours de développement")

if __name__ == "__main__":
    main()
