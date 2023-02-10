from abc import ABC, abstractmethod
from dtos.nave_espacial_dto import NaveDto

class VehiculoEspacialInt(ABC):
    @abstractmethod
    def get_nave(self, nave_id):
        pass
    
    @abstractmethod
    def get_all_naves(self):
        pass
    
    @abstractmethod
    def add_nave(self, nave_dto:NaveDto):
        pass
    
  