from dtos.nave_espacial_dto import NaveDto

class NaveLanzaderaDTO(NaveDto):
    def __init__(self, id, nombre, tipo_propulsion, capacidad_transporte, peso, empuje, altura):
        NaveDto.__init__(self, id, nombre, tipo_propulsion, capacidad_transporte, peso, empuje)
        self.__altura = altura

    def get_altura(self):
        return self.__altura
    
    def set_altura(self, altura):
        self.__altura = altura
        
