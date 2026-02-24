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
