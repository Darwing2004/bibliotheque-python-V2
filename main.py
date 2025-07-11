from bibliotheque import Livre, Bibliotheque

# Création de la bibliothèque avec les infos de connexion
biblio = Bibliotheque(
    host = 'localhost'
    user = 'darwing'
    password ='Boybbswag0@'
    database = 'biblio'
)

#Recuperation des info Utilisateur
titre = input("Entrez le titre du livre : ")
livre = Livre(titre)

# Insertion dans la base
biblio.ajouter_livre(livre)

# Fermeture de la connexion
biblio.fermer()