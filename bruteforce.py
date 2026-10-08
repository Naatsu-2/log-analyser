import os 

def find_successful_bruteforce(chemin , threshold) : 
    alarm = set()
    failure_count = {}

    with open(chemin) as f : 
        for line in f : 
            fields = line.split()
            if len(fields) < 4 : 
                continue
            status = fields[3]
            ip = fields[2]
            if status == "LOGIN_FAIL":
                failure_count[ip] = failure_count.get(ip,0) + 1 
            elif status == "LOGIN_OK" and failure_count.get(ip,0) >= threshold: 
                alarm.add(ip)

    return alarm
            
if __name__ == "__main__" :

    dossier = os.path.dirname(os.path.abspath(__file__))
    chemin = os.path.join(dossier , "connexions.log")

    print(find_successful_bruteforce(chemin, 1))   # {'198.51.100.7', '203.0.113.50'}
    print(find_successful_bruteforce(chemin, 3))   # {'203.0.113.50'}
            
