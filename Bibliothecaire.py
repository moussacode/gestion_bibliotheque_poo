from Adherent import Adherent
class Bibliothecaire:
    def __init__(self):
        self.liste_document= []
        self.liste_adherents = []
       
    def ajout_document(self,document):
        if self.trouver_document(document.titre) is not None:
            print("Document existe deja")
            return False
        
        self.liste_document.append(document)
        print("Document enregistre")
        return True

    def trouver_document(self, titre):
        for document in self.liste_document:
            if document.titre.lower() == titre.lower():
                return document
        return None

    def trouver_adherent(self, nom):
        for adherent in self.liste_adherents:
            if adherent.nom.lower() == nom.lower():
                return adherent
        return None

    def afficher_document(self) :
        if not self.liste_document:
            print("Aucun document enregistre")
            return
        for document in self.liste_document:
            print(document)

    def afficher_adherent(self):
        if not self.liste_adherents:
            print("Aucun adherent enregistre")
            return
        for adherent in self.liste_adherents:
            print(adherent)

    def afficher_emprunt(self):
        if not self.liste_adherents:
            print("Aucun adherent enregistre")
            return
        
        vide = True
        for adherent in self.liste_adherents:
            if adherent.liste_emprunts:
                vide = False
                titres = ", ".join([l.titre for l in adherent.liste_emprunts])
                print(f"{adherent.nom} -> {titres}")
        if vide:
            print("Aucun emprunt enregistre")
       

    def inscrire_membre(self,nom):
        if self.trouver_adherent(nom) is not None:
            print("Adherent deja inscrit")
            return False
        membre = Adherent(nom)
        self.liste_adherents.append(membre)
        print("Adherent ajoute")
        return True

    def valider_pret(self, nom_membre, titre):
        membre = self.trouver_adherent(nom_membre)
        if membre is None:
            print("Le membre n'est pas inscrit")
            return False

        document = self.trouver_document(titre)
        if document is None:
            print("Livre introuvable")
            return False

        if not document.est_disponible:
            print("Livre indisponible")
            return False

        membre.emprunter(document)
        document.marquer_emprunte()
        print("Emprunt enregistre")
        return True
    def recherche_document (self,titre):
        document = self.trouver_document(titre)
        if document is None:
            print("Document introuvable")
            return False
        print(document)
        
    def valider_retour(self, nom_membre, titre):
        membre = self.trouver_adherent(nom_membre)
        if membre is None:
            print("Le membre n'est pas inscrit")
            return False

        document = self.trouver_document(titre)
        if document is None:
            print("Document introuvable")
            return False

        if membre.retourner(document):
            document.marquer_retourne()
            print("Retour enregistre")
            return True
        print("Le membre n'a pas emprunte ce document")
        return False
 