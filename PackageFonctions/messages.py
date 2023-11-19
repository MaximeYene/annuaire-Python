import sqlite3

conn=sqlite3.connect('annuaire_telephonique.db')
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS messages( id INTEGER PRIMARY KEY AUTOINCREMENT, nom_destinataire TEXT, message_envoyé TEXT)")

c.execute("SELECT nom FROM contacts")
contacts=c.fetchall()


def ajout_message():
    nom_destinataire = input('A qui voulez-vous envoyer un message? ')
    
    c.execute("SELECT COUNT(*) FROM contacts WHERE nom=?", (nom_destinataire,))
    existe = c.fetchone()[0]
    
    if existe:
        message_envoyé = input('Entrez votre message : ')
        c.execute("INSERT INTO messages(nom_destinataire, message_envoyé) VALUES (?, ?)", (nom_destinataire, message_envoyé))
        conn.commit()
        print('Message bien emvoyé')
    else:
        print("Il n'y a pas ce nom dans vos contacts.")


def supprimer_message():
    nom_destinataire=input('Quel  est le nom du contact dont vous voulez supprimer le message? ')
    c.execute("SELECT id, message_envoyé FROM messages WHERE nom_destinataire=?",(nom_destinataire,))
    messages_trouvés=c.fetchall()
    if messages_trouvés:
        print(f"Liste des messages envoyés à {nom_destinataire} : ")
        for message in messages_trouvés:
            print(f"ID:{message[0]}, Message:{message[1]}")
    else:
        print(f'Aucun message trouvé pour {nom_destinataire}')

    id=input('Quel est l ID du message que vous voulez supprimer? ')
    c.execute("DELETE FROM messages WHERE id=?",(id,))
    conn.commit()
    print('Message supprimé')

    




