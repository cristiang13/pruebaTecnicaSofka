from dtos.nave_espacial_dto import NaveDto

class NaveTripuladaDTO(NaveDto):
    def __init__(self, id, nombre, tipo_propulsion, capacidad_transporte, peso, empuje, orbita):
        NaveDto.__init__(self, id, nombre, tipo_propulsion, capacidad_transporte, peso, empuje)
        self.__orbita = orbita

    def get_orbita(self):
        return self.__orbita
    
    def set_orbita(self, orbita):
        self.__orbita = orbita