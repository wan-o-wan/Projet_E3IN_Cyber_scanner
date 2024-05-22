#!/usr/bin/env python3

import os
import glob
import sys

# Le premier argument est le nom du script, donc nous prenons le deuxième
main_dir = sys.argv[1]

# Créer le dossier CR
cr_dir = os.path.join("/Pentest", main_dir, "CR")
os.makedirs(cr_dir, exist_ok=True)

# Ouvrir le fichier final pour l'écriture
with open(os.path.join(cr_dir, "CR_final.txt"), 'w') as final_file:
    # Chercher le fichier conf_reseau.txt dans le sous-dossier network_info en premier
    network_info_dir = os.path.join("/Pentest", main_dir, "network_info")
    network_info_file = os.path.join(network_info_dir, "conf_reseau.txt")
    if os.path.isfile(network_info_file):
        final_file.write(f"--- network_info ---\n")
        with open(network_info_file, 'r') as network_info:
            final_file.write(network_info.read())
        final_file.write("\n\n")
    # Chercher le fichier compte_rendu.txt dans le sous-dossier nmap en premier
    nmap_dir = os.path.join(main_dir, "nmap")
    nmap_file = os.path.join(nmap_dir, "compte_rendu.txt")
    if os.path.isfile(nmap_file):
        final_file.write(f"--- nmap ---\n")
        with open(nmap_file, 'r') as compte_rendu:
            final_file.write(compte_rendu.read())
        final_file.write("\n\n")

    # Parcourir tous les autres fichiers compte_rendu.txt dans les sous-dossiers de main_dir
    last_dir = None
    for root, dirs, files in os.walk(main_dir):
        if root == nmap_dir or root == network_info_dir:  # On a déjà traité le sous-dossier nmap et network_info
            continue
        for file in files:
            if file == "compte_rendu.txt":
                current_dir = os.path.dirname(root)
                if current_dir != last_dir:
                    final_file.write(f"\n\n++++++ {os.path.basename(current_dir)} ++++++\n\n")
                    last_dir = current_dir
                # Écrire le nom du sous-dossier dans le fichier final
                final_file.write(f"--- {os.path.basename(root)} ---\n")
                # Ouvrir chaque fichier compte_rendu.txt pour la lecture
                with open(os.path.join(root, file), 'r') as compte_rendu:
                    # Copier le contenu de compte_rendu.txt dans CR_final.txt
                    final_file.write(compte_rendu.read())
                    final_file.write("\n\n")  # Ajouter deux sauts de ligne entre chaque compte rendu