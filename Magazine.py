from Document import Document

class Magazine(Document):
    def __init__(self, titre , theme):
        super().__init__(titre)
        self.theme = theme
        self.type_doc = "Magazine"

    def __str__(self):
        statut = "disponible" if self.est_disponible else "emprunte"
        return (
            f"ID : {self.id_document} | "
            f"Titre {self.titre} | Theme : {self.theme} | Statut : {statut} | Type : {self.type_doc}")
    
    def marquer_emprunte(self):
        self.est_disponible = False
        print(f"Magazine {self.titre} emprunter")

    def marquer_retourne(self):
        self.est_disponible = True
        print(f"Magasine {self.titre}  retourner")
