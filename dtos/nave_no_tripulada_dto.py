from dtos.nave_espacial_dto import NaveDto

class NaveNoTripuladaDTO(NaveDto):
    def __init__(self, id, nombre, tipo_propulsion, capacidad_transporte, peso, empuje):
        super().__init__( id,nombre, tipo_propulsion, capacidad_transporte, peso, empuje)
