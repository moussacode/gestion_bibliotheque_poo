from Bibliothecaire import Bibliothecaire
from Livre import Livre
from Magazine import Magazine

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

