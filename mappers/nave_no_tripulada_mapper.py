from vehiculo_espacial.models import VehiculoNoTripulado
from dtos.nave_no_tripulada_dto import NaveNoTripuladaDTO 

class NaveNoTripuladaMapper:
  def nave_no_tripulada_dto_to_model(nave_dto: NaveNoTripuladaDTO):
    nave= VehiculoNoTripulado(None,nave_dto.get_nombre(),nave_dto.get_tipo_propulsion(),nave_dto.get_capacidad_transporte(),
    nave_dto.get_peso(),nave_dto.get_empuje())
    return nave

  def model_to_nave_no_tripulada_dto(self, nave: VehiculoNoTripulado):
    nave_dto= NaveNoTripuladaDTO(nave.nombre,nave.tipo_propulsion,nave.capacidad_transporte,
    nave.peso,nave.empuje)
    return nave_dto

  def form_to_nave_no_tripulada_dto(input):
    nave_dto= NaveNoTripuladaDTO(None,input['name'][0],input['tipo_propulsion'][0],input['capacidad'][0],
    input['peso'][0],input['empuje'][0]) 
    return nave_dto