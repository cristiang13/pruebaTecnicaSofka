from django.db.models import Q
from dao.interface_nave import VehiculoEspacialInt
from vehiculo_espacial.models import VehiculoLanzadera
from dtos.nave_lanzadera_dto import NaveLanzaderaDTO
from mappers.nave_lanzadera_mapper import NaveLanzaderaMapper

class NaveLanzaderaDao(VehiculoEspacialInt):
    def get_nave(self, nave_id):
        naveMapper= NaveLanzaderaMapper()
        nave = VehiculoLanzadera.objects.get(id=nave_id)
        nave_dto = naveMapper.model_to_nave_lanzadera_dto(nave)
        return nave_dto
    
    def get_all_naves():
        naves = VehiculoLanzadera.objects.all()
        # naves_dto = [NaveLanzaderaDTO(n.id,n.nombre, n.tipo_propulsion, n.capacidad_transporte,n.peso,n.empuje,n.altura) for n in naves]
        return naves
    
    def add_nave(nave_dto:NaveLanzaderaDTO):     
        nave = NaveLanzaderaMapper.nave_lanzadera_dto_to_Model(nave_dto)
        nave.save()
        return nave.nombre
    
    def search(search):
        nave = VehiculoLanzadera.objects.filter(
            Q(nombre__icontains = search)|
            Q(tipo_propulsion__icontains = search)
        ).distinct()
        
        return nave
    

    