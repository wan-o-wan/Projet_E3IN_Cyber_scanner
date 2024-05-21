#!/usr/bin/env python3

import os
import re
import subprocess
import sys

# Le premier argument est le nom du script, donc nous prenons le deuxième
main_dir = sys.argv[1]
# Le dossier contenant vos fichiers
source_dir = os.path.join("/Pentest", main_dir, "80")

# Les chaînes à rechercher
search_string1 = 'NanoCMS v0.4'
dir_name1 = 'nanocms_v0.4'
search_string2 = 'chaîne à rechercher 2'
dir_name2 = 'autre'

# La variable pour stocker les adresses IP
ips = []

for fichier in os.listdir(source_dir):
    ip = re.search(r'80_(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\.txt', fichier)
    if ip:
        ips.append(ip.group(1))


# Faire un wget sur chaque adresse IP et enregistrer le résultat
for ip in ips:
    print(f"Fetching {ip}...")
    # Exécuter la commande wget et enregistrer le résultat dans un fichier
    with open(os.path.join(source_dir, f"{ip}.txt"), "w") as outfile:
        subprocess.run(["wget", "-O-", ip], stdout=outfile)

# Parcourir tous les fichiers dans le dossier source
for filename in os.listdir(source_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(source_dir, filename), 'r') as file:
            # Lire le contenu du fichier
            content = file.read()
            # Utiliser regex pour chercher la première chaîne
            if re.search(search_string1, content):
                print(f"La chaîne '{search_string1}' a été trouvée dans {filename}.")
                # Si la première chaîne est trouvée, créer un fichier vide dans le premier dossier cible
                target_dir1 = os.path.join(source_dir, dir_name1)
                os.makedirs(target_dir1, exist_ok=True)
                open(os.path.join(target_dir1, filename), 'w').close()
                print(f"Le fichier {filename} a été créé dans {target_dir1}.")
            # Utiliser regex pour chercher la deuxième chaîne
            elif re.search(search_string2, content):
                print(f"La chaîne '{search_string2}' a été trouvée dans {filename}.")
                # Si la deuxième chaîne est trouvée, créer un fichier vide dans le deuxième dossier cible
                target_dir2 = os.path.join(source_dir, dir_name2)
                os.makedirs(target_dir2, exist_ok=True)
                open(os.path.join(target_dir2, filename), 'w').close()
                print(f"Le fichier {filename} a été créé dans {target_dir2}.")
