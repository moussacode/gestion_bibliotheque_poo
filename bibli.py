from abc import ABC,abstractmethod

class Document(ABC):
    def __init__(self, titre):
        self.titre = titre
        self.__est_disponible = True
    
    """Protection
    """
    @property
    def est_disponible(self):
        return self.__est_disponible
        
    """Modification de la disponibilite
    """
    
    @est_disponible.setter
    def est_disponible(self,valeur) :
        
        self.__est_disponible = valeur  
       
    
    @abstractmethod
    def marquer_emprunte(self):
        pass
    
    @abstractmethod
    def marquer_retourne(self):
        pass

class Magazine(Document):
    def __init__(self, titre , theme):
        super().__init__(titre)
        self.theme = theme

    def __str__(self):
        statut = "disponible" if self.est_disponible else "emprunte"
        return f"Titre {self.titre} | Theme : {self.theme} | Statut : {statut}"
    
    def marquer_emprunte(self):
        self.est_disponible = False
        print(f"Magazine {self.titre} emprunter")

    def marquer_retourne(self):
        self.est_disponible = True
        print(f"Magasine {self.titre}  retourner")

class Livre(Document):
    def __init__(self, titre,  auteur):
        super().__init__(titre)
        self.auteur = auteur  
    
    def __str__(self):
        statut = "disponible" if self.est_disponible else "emprunte"
        return f"Titre : {self.titre} |Auteur : {self.auteur} | Statut :  {statut}"
    
    def marquer_emprunte(self):
        self.est_disponible = False
        print(f"Livre {self.titre} emprunter")

    def marquer_retourne(self):
        self.est_disponible = True
        print(f"Livre {self.titre}  retourner")
                
class Adherent:
    def __init__(self,nom):
        self.nom = nom
        self.liste_emprunts = []
    
    def __str__(self):
        return f"{self.nom} ({len(self.liste_emprunts)} emprunt(s))"
    
    def emprunter(self, document):
        self.liste_emprunts.append(document)
    
    def retourner(self, document):
        if document in self.liste_emprunts:
            self.liste_emprunts.remove(document)
            return True
        return False

    def lister_emprunts(self):
        return self.liste_emprunts

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
                
class Menu:

    def __init__(self):
        self.bibliotheque = Bibliothecaire()

    def saisir_texte(self, ecrire):
        while True:
            try:
                valeur = input(ecrire).strip()
            except (Exception):

                print("\nSaisie interrompue. Fermeture du programme.")
            if valeur:
                return valeur
            print("Saisie vide, veuillez recommencer.")

    def saisir_choix_menu(self):
        choix_valides = {"1", "2", "3", "4", "5", "6", "7", "8","9","0"}
        while True:
            choix = self.saisir_texte("Choisir:   ")
            if choix in choix_valides:
                return choix
            print("Choix invalide. Entrez un nombre entre 0 et 9.")
    
    def menu(self):
        while True:
            
            print("===========Menu===========")   
            print("1. Ajouter un livre")         
            print("2. Ajouter un Membre")         
            print("3. Valider un emprunt") 
            print("4. Afficher les documents")
            print("5. Afficher les adherants")
            print("6. Liste des emprunts")
            print("7. Retour un document")
            print("8. Ajouter un magazine")
            print("9. Rechercher un document")
            print("0. Quitter")
            choice = self.saisir_choix_menu()

            match choice:
                case "1":
                    titre = self.saisir_texte("Veuillez saisir le titre du livre: ")
                    auteur = self.saisir_texte("Veuillez saisir l'auteur: ")
                    livre = Livre(titre, auteur)
                    self.bibliotheque.ajout_document(livre)


                case "2":
                    nom = self.saisir_texte("Veuillez entrer votre nom: ")
                    self.bibliotheque.inscrire_membre(nom)

                case "3":
                    nom = self.saisir_texte("Veuillez entrer votre nom: ")
                    titre = self.saisir_texte("Veuillez saisir le titre du document: ")
                    self.bibliotheque.valider_pret(nom, titre)
                case "4":
                    self.bibliotheque.afficher_document()
                case "5":
                    self.bibliotheque.afficher_adherent()
                case "6":
                    self.bibliotheque.afficher_emprunt()
                case "7":
                    nom = self.saisir_texte("Veuillez entrer votre nom: ")
                    titre = self.saisir_texte("Veuillez saisir le titre du document: ")
                    self.bibliotheque.valider_retour(nom, titre)
                case "8":
                    titre = self.saisir_texte("Veuillez saisir le titre du magazine: ")
                    theme = self.saisir_texte("Veuillez saisir le theme: ")
                    magazine = Magazine(titre, theme)
                    self.bibliotheque.ajout_document(magazine) 
                case "9":
                    titre = self.saisir_texte("Veuillez saisir le titre du document: ")
                    self.bibliotheque.recherche_document( titre)  
                case "0":
                    print("Au revoir.") 
                    exit()                

menu = Menu()
menu.menu()

