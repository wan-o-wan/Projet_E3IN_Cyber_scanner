import os


#MAJ de l'OS
def update_system():
    os.system("apt-get update")
    os.system("apt-get upgrade")
#MAJ De nmap ainsi que sa bdd de script
# def nmap_update():
    os.system("apt install --only-upgrade nmap -y")
    os.system("nmap --script-updatedb")
#MAJ HASHCAT
# def hashcat_update():
    os.system("apt install --only-upgrade hashcat -y")
#MAJ HYDRA
# def hydra_update():
    os.system("apt install --only-upgrade hydra -y")

update_system()