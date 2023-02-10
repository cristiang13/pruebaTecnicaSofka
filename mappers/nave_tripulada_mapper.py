from vehiculo_espacial.models import VehiculoTripulado
from dtos.nave_tripulada_dto import NaveTripuladaDTO

class NaveTripuladaMapper:
  def nave_tripulada_dto_to_Model(nave_dto: NaveTripuladaDTO):
    nave= VehiculoTripulado(None,nave_dto.get_nombre(),nave_dto.get_tipo_propulsion(),
    nave_dto.get_capacidad_transporte(),nave_dto.get_peso(),nave_dto.get_empuje(),nave_dto.get_orbita())
    return nave

  def model_to_nave_tripulada_dto(nave: VehiculoTripulado):
    nave_dto= NaveTripuladaDTO(nave.nombre,nave.tipo_propulsion,
    nave.capacidad_transporte,nave.peso,nave.empuje,nave.orbita)
    return nave_dto
  
  def form_to_nave_tripulada_dto(input):
    nave_dto= NaveTripuladaDTO(None,input['name'][0],input['tipo_propulsion'][0],
    input['capacidad'][0],input['peso'][0],input['empuje'][0],input['orbita'][0])
    print(nave_dto.get_empuje())
    return nave_dto