import subprocess
import os
import sys
from pathlib import Path

# Le premier argument est le nom du script, donc nous prenons le deuxième
main_dir = sys.argv[1]
# Le dossier contenant vos fichiers
dossier = os.path.join("/Pentest", main_dir,"80")
#dossier = os.path.join("/Pentest/2024-06-13-10-48_Output/80")
# Define the wordlist file
wordlist_file = "/Pentest/outils/wfuzz/test_mot.txt"
# Define the wfuzz directory
wfuzz_dir = os.path.join(dossier, "wfuzz")
# Create the wfuzz directory if it does not exist
os.makedirs(wfuzz_dir, exist_ok=True)
# Define the report file
report_file = os.path.join(wfuzz_dir, "compte_rendu.txt")
Path(report_file).touch

    # Iterate over all files in the main directory
for filename in os.listdir(dossier):
        # If the file is a .txt file
    if filename.endswith(".txt") and not filename.startswith("80"):
            # Get the IP address from the filename
        ip_address = filename[:-4]

            # Generate the target URL
        target_url = f"http://{ip_address}/FUZZ"
        print("Test de wfuzz sur l'adresse", ip_address, ":\n")

        try:
        # Exécute la commande Wfuzz
            command = f"wfuzz -c -z file,{wordlist_file} {target_url} >> {report_file}"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            print(result.stdout)

        # Affiche la sortie
            print("la commande c'est correctement terminer pour l'ip ", ip_address, ":\n")
        except Exception as e:
            print(f"Erreur lors de l'exécution de Wfuzz : {e}")
'''
# Define a function to remove banners from the file
def edit_compte_rendu(report_file):
    with open(report_file, "r") as file:
        lines = file.readlines()

    with open(report_file, "w") as file:
        for line in lines:
            # If the line does not start with "*" (which is the start of the banner), write it to the file
            if not line.startswith("*"):
                file.write(line)

# Call the function to remove banners from "compte_rendu.txt"

# edit_compte_rendu(report_file)
'''