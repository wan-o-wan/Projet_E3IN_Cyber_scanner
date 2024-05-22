import os
import socket
import subprocess
import time

def check_dhcp():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return None

def set_nameserver():
    try:
        os.system("echo 'nameserver 8.8.8.8' >> /etc/resolv.conf")
        print("Le nameserver a été ajouté au fichier /etc/resolv.conf.")
    except Exception as e:
        print("Échec de l'ajout du nameserver : " + str(e))

def ping(ip):
    print("Essai de ping à l'adresse : " + ip)
    try:
        output = subprocess.check_output("ping -c 1 " + ip, shell=True)
        output = output.decode('utf-8')
        with open('ping.txt', 'a') as f:
            f.write(output)
        if '1 packets transmitted, 1 received' in output:
            return True
        else:
            return False
    except Exception:
        return False

def set_ip(ip):
    print ("Configuration de l'adresse IP : " + ip)
    try:
        os.system("ip link set ens192 up")
        os.system("ip addr flush dev ens192")
        os.system("ip addr add " + ip + "/24 dev ens192")
        time.sleep(5)
    except Exception as e:
        print("Failed to set IP: " + str(e))

def set_default_route(gateway_ip):
    print("Configuration de la route par défaut avec l'adresse : " + gateway_ip)
    try:
        os.system("ip route add default via " + gateway_ip)
        print("La passerelle par défaut a été configurée avec l'adresse IP : " + gateway_ip)
    except Exception as e:
        print("Échec de la configuration de la route par défaut : " + str(e))

def check_networks():
    with open('ip_test.txt','w') as f:
        for i in range(17, 19):
            for j in range(7, 9):
                ip = "10." + str(i) + "." + str(j) + ".97"
                print("Test de l'IP : " + ip)
                f.write(ip+'\n')
                set_ip(ip)
                if ping(ip[:-3] + ".1"):
                    set_default_route(ip[:-3] + ".1")
                    return ip
                elif ping(ip[:-3] + ".254"):
                    set_default_route(ip[:-3] + ".254")
                    return ip
            #ip = "192.168." + str(i) + ".97"
            #print("Test de l'IP : " + ip)
            #set_ip(ip)
            #if ping(ip[:-3] + ".1") or ping(ip[:-3] + ".254"):
            #    return ip
    return None

def main():
    ip = check_dhcp()
    if ip is None:
        print("Pas de DHCP, vérification des réseaux privés...")
        ip = check_networks()
        if ip is None:
            print("Aucun réseau trouvé.")
        else:
            print("Réseau trouvé à l'IP : " + ip)
    else:
        print("Connecté avec DHCP à l'IP : " + ip)

if __name__ == "__main__":
    main()
    set_nameserver()
