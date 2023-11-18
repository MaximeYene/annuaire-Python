import sqlite3
conn=sqlite3.connect('annuaire_telephonique.db')
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS contacts(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, numero TEXT)")




def ajouter_contact():
    nom = input("Nom du contact : ")
    numero = input("Numéro de téléphone : ")
    c.execute("INSERT INTO contacts (nom, numero) VALUES (?, ?)", (nom, numero))
    conn.commit()


def supprimer_contact():
    nom = input("Nom du contact à supprimer : ")
    c.execute("DELETE FROM contacts WHERE nom = ?", (nom,))
    conn.commit()


def modifier_contact():
    nom = input("Nom du contact à modifier : ")
    nouveau_nom = input("Nouveau nom du contact : ")
    nouveau_numero = input("Nouveau numéro de téléphone : ")
    c.execute("UPDATE contacts SET nom = ?, numero = ? WHERE nom = ?", (nouveau_nom, nouveau_numero, nom))
    conn.commit()


def rechercher_contact():
    nom = input("Nom du contact à rechercher : ")
    c.execute("SELECT * FROM contacts WHERE nom = ?", (nom,))
    results = c.fetchall()



    for result in results:
        print(result)



def afficher_tous_les_contacts():
    c.execute("SELECT * FROM contacts")
    results = c.fetchall()

    for result in results:
        print(result)

