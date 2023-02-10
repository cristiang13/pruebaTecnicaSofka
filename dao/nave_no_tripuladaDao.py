from django.db.models import Q
from dao.interface_nave import VehiculoEspacialInt
from vehiculo_espacial.models import VehiculoNoTripulado
from dtos.nave_no_tripulada_dto import NaveNoTripuladaDTO
from mappers.nave_no_tripulada_mapper import NaveNoTripuladaMapper

class NaveNoTripuladaDao(VehiculoEspacialInt):
    
    def get_nave(self, nave_id):
        pass
    
    def get_all_naves():
        naves = VehiculoNoTripulado.objects.all()
        return naves
    def add_nave(nave_dto:NaveNoTripuladaDTO):     
        nave = NaveNoTripuladaMapper.nave_no_tripulada_dto_to_model(nave_dto)
        nave.save()
        return nave
    
    def search(search):
        nave = VehiculoNoTripulado.objects.filter(
            Q(nombre__icontains = search)|
            Q(tipo_propulsion__icontains = search)
        ).distinct()
        return nave