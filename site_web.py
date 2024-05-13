#!/usr/bin/env python3

import os
import re

# Le dossier contenant les fichiers 'ip.txt'
source_dir = '/home/erwan/Pentest/Output/web_80'

# Les dossiers où vous voulez déplacer les fichiers
target_dir1 = '/home/erwan/Pentest/Output/web_80/nanocms_v0.4'
target_dir2 = '/home/erwan/Pentest/Output/web_80/autre'

# Les chaînes à rechercher
search_string1 = 'NanoCMS v0.4'
search_string2 = 'chaîne à rechercher 2'

# Parcourir tous les fichiers dans le dossier source
for filename in os.listdir(source_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(source_dir, filename), 'r') as file:
            # Lire le contenu du fichier
            content = file.read()
            # Utiliser regex pour chercher la première chaîne
            if re.search(search_string1, content):
                # Si la première chaîne est trouvée, créer un fichier vide dans le premier dossier cible
                open(os.path.join(target_dir1, filename), 'w').close()            # Utiliser regex pour chercher la deuxième chaîne
            elif re.search(search_string2, content):
                # Si la deuxième chaîne est trouvée, créer un fichier vide dans le deuxième dossier cible
                open(os.path.join(target_dir2, filename), 'w').close()
