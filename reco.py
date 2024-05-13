#!/usr/bin/env python3

import subprocess
import datetime
import re

# Obtenir la date actuelle
#now = datetime.datetime.now().strftime("%Y-%m-%d")

# Exécuter la commande nmap
nmap_output = subprocess.check_output(["nmap", "-sV", "10.17.8.0/24"]).decode()

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
        with open(f"/home/erwan/Pentest/Output/nmap/{port}_{host}.txt", 'a') as f:
            f.write(port + ' ' + host + '\n' + line + '\n')

