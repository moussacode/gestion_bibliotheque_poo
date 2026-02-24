from Document import Document

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
