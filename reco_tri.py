#!/usr/bin/env python3

import os
import subprocess
import re
import sys
#from main_pentest import main_dir

# Le premier argument est le nom du script, donc nous prenons le deuxième
main_dir = sys.argv[1]
# Le dossier contenant vos fichiers
dossier = os.path.join("/Pentest", main_dir)

# Créer un dossier pour nmap s'il n'existe pas déjà
nmap_dir = os.path.join(dossier, 'nmap')
if not os.path.exists(nmap_dir):
    os.makedirs(nmap_dir, exist_ok=True)
    print(f"Le dossier {nmap_dir} a été créé avec succès.")
else:
    print(f"Le dossier {nmap_dir} existe déjà.")

print("Execution de nmap")
try:
    # Exécuter la commande nmap
    nmap_output = subprocess.check_output(["nmap", "-sV", "10.17.8.0/24"]).decode()
    print("La commande nmap s'est exécutée avec succès.")
except subprocess.CalledProcessError as e:
    print(f"La commande nmap a échoué avec l'erreur : {e}")

# Enregistrer la sortie de nmap dans un fichier
with open(os.path.join(nmap_dir, 'nmap_output.txt'), 'w') as f:
    f.write(nmap_output)
    print("La sortie de nmap a été enregistrée avec succès dans le fichier nmap_output.txt.")

# Séparer le résultat de nmap par ligne
lines = nmap_output.split('\n')

host = ''
for line in lines:
    # Vérifier si la ligne contient un hôte
    if 'Nmap scan report for' in line:
        host = line.split(' ')[4]

    # Vérifier si la ligne contient un port ouvert
    if re.search(r'\d+/tcp\s+open', line):
        port = line.split('/')[0]

        # Créer un dossier pour le port s'il n'existe pas déjà
        port_dir = os.path.join(dossier, port)
        if not os.path.exists(port_dir):
            os.makedirs(port_dir, exist_ok=True)
            print(f"Le dossier {port_dir} a été créé avec succès.")
        else:
            print(f"Le dossier {port_dir} existe déjà.")
        
        # Créer le fichier dans le dossier du port
        with open(f"{port_dir}/{port}_{host}.txt", 'a') as f:
            f.write(port + ' ' + host + '\n' + line + '\n')


   #Tri du fichier nmap 
    with open(os.path.join(nmap_dir, 'nmap_output.txt'), 'r') as f, open(os.path.join(nmap_dir, 'compte_rendu.txt'), 'w') as out:    
        copy = False
        for line in f:
            if line.startswith('Nmap scan report for'):
                if copy:  # Ajoute un saut de ligne entre chaque hôte
                    out.write('\n')
                copy = True
                out.write(line)
            elif line.strip() == '':
                copy = False
            elif copy:
                if ("/tcp" in line and line.split('/')[1].startswith('tcp')) or line.startswith('Service Info'):                    
                    out.write(line)

