import mysql.connector


class Livre:
    def __init__(self, titre):
        self.titre = titre


class Bibliotheque:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )

        self.cursor = self.conn.cursor()

    def ajouter_livre(self, livre):
        query = "INSERT INTO livres (titre) VALUES (%s)"
        self.cursor.execute(query, (livre.titre,))
        self.conn.commit()
        print("Livre insere avec succes !")

    def fermer(self):
        self.cursor.close()
        self.conn.close()
