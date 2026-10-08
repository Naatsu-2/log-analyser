import os 

def count_failure (chemin): 
    """Return a dictionary with the number of failed connections for each IP address"""
    failure_count = {}
    with open (chemin) as f : 
        for line in f : 
            fields = line.split()
            if len(fields) < 4 : 
                continue
            if fields[3] == "LOGIN_FAIL":
                ip = fields[2]
                failure_count[ip] = failure_count.get(ip,0) + 1 
    return failure_count

if __name__ == "__main__" :

    dossier = os.path.dirname(os.path.abspath(__file__))
    chemin = os.path.join(dossier , "connexions.log")
    print (count_failure(chemin))