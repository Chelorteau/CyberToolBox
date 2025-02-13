import streamlit as st
import ipaddress
import pandas as pd

def run():
    st.header("🛠️ Calculateur FLSM/VLSM")

    # Saisie de l'adresse IP et du nombre de sous-réseaux
    ip_input = st.text_input("Entrez l'adresse réseau (ex: 192.168.1.0/24)").strip()
    subnetting_type = st.radio("Choisissez le type de subnetting", ["FLSM", "VLSM"])

    if subnetting_type == "FLSM":
        num_subnets = st.number_input("Nombre de sous-réseaux", min_value=1, step=1)

        if st.button("Calculer"):
            try:
                network = ipaddress.ip_network(ip_input, strict=False)
                prefix_length = network.prefixlen
                new_prefix = prefix_length + (num_subnets - 1).bit_length()

                if new_prefix > 32:
                    st.error("Impossible de créer ce nombre de sous-réseaux avec cette adresse réseau.")
                else:
                    subnets = list(network.subnets(new_prefix=new_prefix))
                    st.success(f"Création de {len(subnets)} sous-réseaux avec le préfixe /{new_prefix}")

                    # Construction du tableau des sous-réseaux
                    data = []
                    for i, subnet in enumerate(subnets, 1):
                        subnet_mask = ipaddress.IPv4Network(subnet).netmask
                        data.append({
                            "Numéro du sous-réseau": f"Sous-réseau {i}",
                            "Adresse sous-réseau": str(subnet),
                            "Masque": str(subnet_mask)
                        })

                    df = pd.DataFrame(data)
                    st.table(df)

            except ValueError as e:
                st.error(f"Erreur: {e}")

    elif subnetting_type == "VLSM":
        st.write("🔍 Fonctionnalité en cours de développement")
