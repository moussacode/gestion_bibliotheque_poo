from Adherent import Adherent
from Livre import Livre
from Magazine import Magazine

class Bibliothecaire:
    def __init__(self,db):
        self.liste_document= []
        self.liste_adherents = []
        self.db = db
       
    def ajout_document(self,document):
        cursor = self.db.connection.cursor()
        query = """
        INSERT INTO documents (titre, type, auteur, theme, est_disponible)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            document.titre,
            document.type_doc,
            document.auteur,
            document.theme,
            document.est_disponible
        ))

        self.db.connection.commit()
        print("Document ajouté avec succès ")
        return True

    def trouver_document(self, id_document):
        try :
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM documents where id_document  = %s",(id_document,))
            row = cursor.fetchone()
            
            if row["type"] == "Livre":
                doc = Livre(row["titre"], row["auteur"])
            else:
                doc = Magazine(row["titre"], row["theme"])
            doc.est_disponible = row["est_disponible"]

            return doc
        except Exception :
            return None


        

        

    def trouver_adherent(self, id_adherent):
        try: 
            cursor = self.db.connection.cursor()
            cursor.execute(
            "SELECT 1 FROM adherents WHERE id_adherent = %s",
            (id_adherent,)
        )
            row = cursor.fetchone()
            return row
        except Exception :
            return None

    def afficher_document(self) :
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM documents")
        rows = cursor.fetchall()
        for row in rows:
            if row["type"] == "Livre":
                doc = Livre(row["titre"], row["auteur"])
            else:
                doc = Magazine(row["titre"], row["theme"])
            doc.est_disponible = row["est_disponible"]
            doc.id_document = row["id_document"] 
            self.liste_document.append(doc)
        if not self.liste_document:
            print("Aucun document enregistre")
            return
        for document in self.liste_document:
            print(document)

    def afficher_adherent(self):
        
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM adherents")
        rows = cursor.fetchall()
        for row in rows:
            membre = Adherent(row["nom"])
            self.liste_adherents.append(membre)
        if not self.liste_adherents:
            print("Aucun adherent enregistre")
            return
        for document in self.liste_adherents:
            print(document)

    def afficher_emprunt(self):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("select E.id_emprunt, D.id_document , D.titre ,A.nom from emprunts E Join Documents D on D.id_document = E.id_document join Adherents A On A.id_adherent = E.id_adherent where D.est_disponible= False")
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row['id_emprunt']} | {row['titre']} {row['nom']}")
            
        
       

    def inscrire_membre(self,nom):
        
        cursor = self.db.connection.cursor()
        query = """
        INSERT INTO adherents (nom)
        VALUES (%s)
        """
        cursor.execute(query, (
            nom,  
        ))

        self.db.connection.commit()
        print("Adherent ajoute")
        return True

    def valider_pret(self, id_adherent, id_document):
        membre = self.trouver_adherent(id_adherent)
        if membre is None:
            print("Le membre n'est pas inscrit")
            return False

        document = self.trouver_document(id_document)
        if document is None:
            print("Livre introuvable")
            return False

        if not document.est_disponible:
            print("Livre indisponible")
            return False
        
        
        cursor = self.db.connection.cursor()
        query = """
        INSERT INTO emprunts (id_adherent, id_document)
        VALUES (%s,%s)
        """
        cursor.execute(query, (
            id_adherent, id_document  
        ))
        cursor.execute(
                "UPDATE documents SET est_disponible = %s WHERE id_document = %s",
                (False, id_document)
            )
        self.db.connection.commit()
        print("Emprunt enregistre")
        return True
        
    def recherche_document (self,id_document):
        document = self.trouver_document(id_document)
        if document is None:
            print("Document introuvable")
            return False
        print(document)
        
    def valider_retour(self, id_adherent, id_document):
        membre = self.trouver_adherent(id_adherent)
        if membre is None:
            print("Le membre n'est pas inscrit")
            return False

        document = self.trouver_document(id_document)
        if document is None:
            print("Document introuvable")
            return False

        cursor = self.db.connection.cursor()
        
        cursor.execute(
                "UPDATE documents SET est_disponible = %s WHERE id_document = %s",
                (True, id_document)
            )
        self.db.connection.commit()
        print("Retour enregistre")
        return True
        # print("Le membre n'a pas emprunte ce document")
        # return False
 