import csv
import sqlite3 as sgbd

cnx = sgbd.connect("/home/tnsi-eleve3/mediatheque.db")
c=cnx.cursor()
c.execute("SELECT * FROM usager")
r=c.fetchall()

with open("usager.csv", "w") as f :
    csvf = csv.writer(f)
    for elem in r :
        csvf.writerows(list(elem))