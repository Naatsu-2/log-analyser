import os 
from count_failure import count_failure
from count_ip import count_ip
from bruteforce import find_successful_bruteforce
from suspicious_ips import suspicious_ips

if __name__ == "__main__" : 

    dossier = os.path.dirname(os.path.abspath(__file__))
    chemin = os.path.join(dossier, "connexions.log")

    print("Connections per IP:", count_ip(chemin))
    print("Failed logins per IP:", count_failure(chemin))
    print("Suspicious IPs:", suspicious_ips(count_failure(chemin), 3))
    print("Successful brute force:", find_successful_bruteforce(chemin, 3))