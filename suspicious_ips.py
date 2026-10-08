import os 
from count_failure import count_failure

def suspicious_ips (failure_count, threshold) :
    """Return the IPs with at least 'threshold' failed logins"""
    return [ip for ip, n in failure_count.items() if n >= threshold]

if __name__ == "__main__" : 

    dossier = os.path.dirname(os.path.abspath(__file__))
    chemin = os.path.join(dossier , "connexions.log")

    failure_count = count_failure(chemin)
    
    print(suspicious_ips(failure_count, 3))   # ['203.0.113.50']
    print(suspicious_ips(failure_count, 1))   # ['203.0.113.50', '198.51.100.7']