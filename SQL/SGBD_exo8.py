import sqlite3 as sgbd

class Usager :
    def __init__(self, code_barre):
        self.cnx = sgbd.connect("/home/tnsi-eleve3/mediatheque.db")
        self.c = self.cnx.cursor()
        self.cb = code_barre

    def __del__(self):
        self.cnx.close()

    def emprunter(self, isbn):
        e=self.c.execute("INSERT INTO emprunt VALUES ? , ? , SELECT  date('now'+ 30)", [self.cb, isbn])
        return e.fetchall()

    def rendre(self, isbn):
        e=self.c.execute("DELETE FROM emprunts WHERE isbn = ?", [isbn])
        return e.fetchall()

    def emprunts(self):
        e=self.c.execute('''SELECT livre.titre, emprunt.isbn, emprunt.retour 
                         FROM emprunt INNER JOIN livre ON emprunt.isbn =livre.isbn 
                         WHERE emprunt.code_barre = ?''', [self.cb])
        return e.fetchall()

    