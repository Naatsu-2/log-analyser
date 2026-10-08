import os


def count_ip (chemin) :
    """Return a dictionary with the number of connections for each IP address"""
    ip_count = {}
    with open(chemin) as f:
        for line in f:
            fields = line.split()
            if len(fields) < 3 :
                continue
            ip = fields[2]
            ip_count[ip] = ip_count.get(ip,0) + 1
    return ip_count

if __name__ == "__main__":

    """Putting the path of the file in a variable to avoid problems with the path when running the script from another directory"""
    dossier = os.path.dirname(os.path.abspath(__file__))
    chemin = os.path.join(dossier,"connexions.log")

    print (count_ip(chemin))


""" from pathlib import Path
chemin = Path(__file__).parent / "connexions.log" ( Same thing but more modern)"""