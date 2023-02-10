from vehiculo_espacial.models import VehiculoLanzadera
from dtos.nave_lanzadera_dto import NaveLanzaderaDTO 

class NaveLanzaderaMapper:
  def nave_lanzadera_dto_to_Model( nave_dto: NaveLanzaderaDTO):
    nave= VehiculoLanzadera(None,nave_dto.get_nombre(),nave_dto.get_tipo_propulsion(),nave_dto.get_capacidad_transporte(),
    nave_dto.get_peso(),nave_dto.get_empuje(),nave_dto.get_altura())
   
    return nave

  def model_to_nave_lanzadera_dto(self, nave: VehiculoLanzadera):
    nave_dto= NaveLanzaderaDTO(nave.nombre,nave.tipo_propulsion,nave.capacidad_transporte,nave.peso,
    nave.empuje,nave.altura)
    return nave_dto
  
  def form_to_nave_lanzadera_dto(input):
      nave_dto= NaveLanzaderaDTO(None,input['name'][0],input['tipo_propulsion'][0],
      input['capacidad'][0],input['peso'][0],input['empuje'][0],input['altura'][0])
      return nave_dto
  
  def naves_lanzadera_dto_To_list(naves_dto: NaveLanzaderaDTO):
      list={}   
      nave_dto= NaveLanzaderaDTO(None,input['name'][0],input['tipo_propulsion'][0],
      input['capacidad'][0],input['peso'][0],input['empuje'][0],input['altura'][0])
      return nave_dto    
      