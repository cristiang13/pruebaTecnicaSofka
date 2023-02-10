from django.db.models import Q
from dao.interface_nave import VehiculoEspacialInt
from vehiculo_espacial.models import VehiculoTripulado
from dtos.nave_tripulada_dto import NaveTripuladaDTO
from mappers.nave_tripulada_mapper import NaveTripuladaMapper

class NaveTripuladaDao(VehiculoEspacialInt):
    
    def get_nave(self, nave_id):
        pass
    
    def get_all_naves():
        naves = VehiculoTripulado.objects.all()
        # naves_dto = [NaveTripuladaDTO(n.id,n.nombre, n.tipo_propulsion, n.capacidad_transporte,n.peso,n.empuje,n.orbita) for n in naves]
        return naves
    def add_nave(nave_dto:NaveTripuladaDTO):     
        nave = NaveTripuladaMapper.nave_tripulada_dto_to_Model(nave_dto)
        nave.save()
        return nave
    
    def search(search):
        nave = VehiculoTripulado.objects.filter(
            Q(nombre__icontains = search)|
            Q(tipo_propulsion__icontains = search)           
        ).distinct()
        
        return nave