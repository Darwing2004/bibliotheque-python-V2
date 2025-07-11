import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="darwing",
    password="Boybbswag0@",
    database="biblio"
)

cursor = conn.cursor()

titre = input("Entrez le titre du livre : ")

query = "INSERT INTO livres (titre) VALUES (%s)"
cursor.execute(query, (titre,))

conn.commit()

print("Livre inséré avec succès !")

cursor.close()
conn.close()
