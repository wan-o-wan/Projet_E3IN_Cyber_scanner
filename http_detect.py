#!/usr/bin/env python3

import os
import re
import subprocess

# Le dossier contenant vos fichiers
dossier = '/home/erwan/Pentest/Output/nmap/'

# La variable pour stocker les adresses IP
ips = []

# Parcourir tous les fichiers dans le dossier
for fichier in os.listdir(dossier):
   # print(fichier)
    # Vérifier si le fichier commence par "80"
    if fichier.startswith('80') and fichier.endswith('.txt'):
        # Extraire l'adresse IP du nom du fichier
       # print(fichier)
        ip = re.search(r'80_(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\.txt', fichier)
        if ip:
            ips.append(ip.group(1))

# Afficher les adresses IP extraites
# for ip in ips:
#    print(ip)

    # Faire un wget sur chaque adresse IP et enregistrer le résultat
for ip in ips:
    print(f"Fetching {ip}...")
    # Exécuter la commande wget et enregistrer le résultat dans un fichier
    with open(f"/home/erwan/Pentest/Output/web_80/{ip}.txt", "w") as outfile:
        subprocess.run(["wget", "-O-", ip], stdout=outfile)

    # Créer un fichier pour le compte rendu
with open(os.path.join(source_dir, 'compte_rendu.txt'), 'w') as compte_rendu:
    # Parcourir tous les fichiers dans le dossier source
    for filename in os.listdir(source_dir):
        if filename.endswith('.txt') and re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.txt', filename):
            # Extraire l'adresse IP du nom du fichier
            ip = filename.replace('.txt', '')
            # Lire le nom d'utilisateur
            with open(os.path.join(source_dir, 'login.txt'), 'r') as login_file:
                username = login_file.read().strip()
            # Lire le mot de passe déchiffré
            with open(os.path.join(source_dir, 'decrypter.txt'), 'r') as decrypter_file:
                decrypted_password = decrypter_file.read().strip()
            # Écrire le compte rendu dans le fichier
            compte_rendu.write(f'Hôte (IP) : {ip}\n')
            compte_rendu.write(f'Nom d\'utilisateur : {username}\n')
            compte_rendu.write(f'Mot de passe déchiffré : {decrypted_password}\n\n')
