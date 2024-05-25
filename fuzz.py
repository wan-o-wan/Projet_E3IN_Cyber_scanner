import subprocess

def wfuzz_discovery(target_url, wordlist_path):
    """
    Utilise Wfuzz pour découvrir les répertoires et fichiers cachés sur un site web.
    :param target_url: L'URL cible (par exemple, "http://votre-site.com/FUZZ").
    :param wordlist_path: Chemin vers votre liste de mots (fichier texte).
    """
    try:
        # Exécute la commande Wfuzz
        command = f"wfuzz -c -z file,{wordlist_path} {target_url}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Affiche la sortie
        print(result.stdout)
    except Exception as e:
        print(f"Erreur lors de l'exécution de Wfuzz : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    target_url = "http://votre-site.com/FUZZ"
    wordlist_path = "/chemin/vers/votre/wordlist.txt"  # Remplacez par le chemin de votre liste de mots
    wfuzz_discovery(target_url, wordlist_path)
