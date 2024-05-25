import subprocess
import re

def run_theharvester(company_domain):
    """
    Utilise TheHarvester pour collecter des informations sur une entreprise.
    :param company_domain: Domaine de l'entreprise (par exemple, "votre-entreprise.com").
    """
    try:
        # 1. Collecte d'informations sur le domaine
        command = f"theharvester -d {company_domain} -l 100 -b all"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # 2. Analyse des sous-domaines
        subdomains = re.findall(r"\b(?:a-z0-9?\.)+[a-z]{2,6}\b", result.stdout)
        print(f"Sous-domaines associés à {company_domain} :")
        for subdomain in subdomains:
            print(subdomain)

        # 3. Recherche d'adresses e-mail
        email_addresses = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", result.stdout)
        print(f"Adresses e-mail associées à {company_domain} :")
        for email in email_addresses:
            print(email)

        # 4. Recherche d'employés sur LinkedIn
        linkedin_profiles = re.findall(r"linkedin\.com/in/([a-zA-Z0-9-]+)", result.stdout)
        print(f"Profils LinkedIn d'employés de {company_domain} :")
        for profile in linkedin_profiles:
            print(f"https://linkedin.com/in/{profile}")
    except Exception as e:
        print(f"Erreur lors de l'exécution de TheHarvester : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    company_domain = "votre-entreprise.com"  # Remplacez par le domaine de l'entreprise cible
    run_theharvester(company_domain)
