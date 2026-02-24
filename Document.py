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
