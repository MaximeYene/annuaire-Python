import sqlite3

conn=sqlite3.connect('annuaire_telephonique.db')
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS messages( id INTEGER PRIMARY KEY AUTOINCREMENT, nom_destinataire TEXT, message_envoyé TEXT)")

c.execute("SELECT nom FROM contacts")
contacts=c.fetchall()


def ajout_message():
    nom_destinataire=input('A qui voulez vous envoyer un message? ')
    for nom_destinataire in contacts:
        message_envoyé=input('Entrez votre message : ')
        c.execute("INSERT INTO messages(nom_destinataire, message_envoyé) VALUES (?, ?)",(nom_destinataire, message_envoyé))
        conn.commit()


