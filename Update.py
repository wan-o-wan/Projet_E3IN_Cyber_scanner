import os


#MAJ de l'OS
def update_system():
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")
#MAJ De nmap ainsi que sa bdd de script
# def nmap_update():
    os.system("sudo apt install --only-upgrade nmap")
    os.system("sudo nmap --script-updatedb")
#MAJ HASHCAT
# def hashcat_update():
    os.system("sudo apt install --only-upgrade hashcat")
#MAJ HYDRA
# def hydra_update():
    os.system("sudo apt install --only-upgrade hydra")

update_system()