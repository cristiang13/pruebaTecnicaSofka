from django.shortcuts import render,redirect
from mappers.nave_lanzadera_mapper import NaveLanzaderaMapper
from mappers.nave_no_tripulada_mapper import NaveNoTripuladaMapper
from mappers.nave_tripulada_mapper import NaveTripuladaMapper
from dao.nave_lanzaderaDao import NaveLanzaderaDao
from dao.nave_tripuladaDao import NaveTripuladaDao
from dao.nave_no_tripuladaDao import NaveNoTripuladaDao

# Función para mostrar la página de inicio
def home(request):
    return render(request, 'home.html')

# Función para mostrar la página para agregar una nave
def add_nave(request):
    return render(request, 'naves_espaciales/add_nave.html')

# Función que almacena una nave recibida desde el formulario
def store_nave(request):
    inputs = dict(request.POST)
    if inputs['categoria'][0] == "nave_no_tripulada":
        nave_dto= NaveNoTripuladaMapper.form_to_nave_no_tripulada_dto(inputs)
        NaveNoTripuladaDao.add_nave(nave_dto)
    if inputs['categoria'][0]=="nave_tripulada":
        nave_dto= NaveTripuladaMapper.form_to_nave_tripulada_dto(inputs)
        NaveTripuladaDao.add_nave(nave_dto)
    if inputs['categoria'][0]=="nave_lanzadera":
        nave_dto= NaveLanzaderaMapper.form_to_nave_lanzadera_dto(inputs)
        NaveLanzaderaDao.add_nave(nave_dto)
    return redirect(add_nave)
# funcion para mostrar la pagina de busqueda 
def search(request):
    return render(request, 'naves_espaciales/search_nave.html')

# funcion que muestra la busqueda 
def get_naves(request):
    inputs = dict(request.GET)
    categoria = request.GET.get('categoria')
    search = request.GET.get('buscar')
    if search:
        categoria= request.GET.get('categoria_search')
        print(request.GET)
       
    name=['id','nombre','Tipo de Propulsion','Capacidad','Peso(kg)','Empuje(Kg)']
    
    if categoria == '1':
        if search and search.strip() != "":
            get_naves = NaveNoTripuladaDao.search(search)
        else:
            get_naves = NaveNoTripuladaDao.get_all_naves()
        name=name   
    if categoria == '2':
        if search and search.strip() != "":
            get_naves = NaveTripuladaDao.search(search)
        else:
            get_naves=NaveTripuladaDao.get_all_naves()
        name.append('Orbita')       
    if categoria == '3':
        if search and search.strip() != "":
            get_naves = NaveLanzaderaDao.search(search)
            print("search view ",get_naves)
        else:
            get_naves=NaveLanzaderaDao.get_all_naves()
        name.append('Altura')
        
    print(categoria,"hoarade")
    context={
    'list_naves':get_naves,
    'name':name,
    'categoria':categoria
    }
    return render(request, 'naves_espaciales/search_nave.html',context=context)
    
    



