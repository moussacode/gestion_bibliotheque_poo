from Document import Document

class Livre(Document):
    def __init__(self, titre,  auteur):
        super().__init__(titre)
        self.auteur = auteur  
        self.type_doc = "Livre"
    
    def __str__(self):
        statut = "disponible" if self.est_disponible else "emprunte"
        return (
            f"ID : {self.id_document} | "
            f"Titre : {self.titre} | "
            f"Auteur : {self.auteur} | "
            f"Statut : {statut} | "
            f"Type : {self.type_doc}"
        )
    def marquer_emprunte(self):
        self.est_disponible = False
        print(f"Livre {self.titre} emprunter")

    def marquer_retourne(self):
        self.est_disponible = True
        print(f"Livre {self.titre}  retourner")
 