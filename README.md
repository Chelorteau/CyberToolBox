# CyberToolbox - Outils de Cybersécurité

CyberToolbox est une application développée avec Streamlit pour regrouper divers outils utiles en cybersécurité, comme le calcul d'adressage IP (FLSM/VLSM), le scan de ports, l'analyse de paquets et d'autres fonctionnalités.

## 📦 Fonctionnalités

- **Réseau**
  - Calcul FLSM/VLSM
  - Analyse de paquets
  - Scan de ports
- **BruteForce**
  - Générateur de mots de passe (à venir)
  - Crackeur de hachage (à venir)
- **Forensics**
  - Analyse de journaux (à venir)
  - Extraction de métadonnées (à venir)
- **Outils Divers**
  - Convertisseur d'encodage (à venir)
  - Calculateur de checksum (à venir)

## 🚀 Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/Chelorteau/CyberToolBox
cd CyberToolbox
```

2. Créez un environnement virtuel et activez-le :
```bash
python -m venv venv
source venv/bin/activate  # Sur Linux/Mac
venv\Scripts\activate    # Sur Windows
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## 🖥️ Utilisation

Lancez l'application avec :
```bash
streamlit run main.py
```

Ensuite, ouvrez un navigateur et accédez à l'URL indiquée (par défaut `http://localhost:8501`).

## ⚙️ Structure du projet

```
CyberToolbox/
    ├── main.py                # Interface principale avec Streamlit
    ├── tools/
    │    ├── flsm_vlsm.py      # Outil de calcul d'adressage
    │    ├── port_scanner.py   # Outil de scan de ports
    │    ├── packet_analyzer.py# Analyse de paquets
    │    └── __init__.py
    ├── utils/
    │    └── helpers.py        # Fonctions d'aide et utilitaires
    ├── resources/
    │    └── images/           # Illustrations et schémas
    └── requirements.txt        # Liste des dépendances
```

## 🔍 Exemples

- **Calcul FLSM** : Saisissez une adresse IP (ex: `192.168.1.0/24`), choisissez `FLSM` et indiquez le nombre de sous-réseaux. Le résultat s'affichera sous forme de tableau avec les sous-réseaux et leurs masques.

## 🛠️ Technologies

- Python
- Streamlit
- ipaddress
- pandas

---

🚀 **CyberToolbox** - Votre boîte à outils en cybersécurité !

