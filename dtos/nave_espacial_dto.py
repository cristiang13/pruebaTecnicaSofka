

class NaveDto:  
    def __init__(self, id, nombre, tipo_propulsion,capacidad_transporte,peso, empuje):
            self.__id = id
            self.__nombre = nombre
            self.__tipo_propulsion = tipo_propulsion
            self.__capacidad_transporte = capacidad_transporte
            self.__peso = peso
            self.__empuje = empuje 

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_tipo_propulsion(self):
        return self.__tipo_propulsion
    
    def set_tipo_propulsion(self, tipo_propulsion):
        self.__tipo_propulsion = tipo_propulsion
        
    def get_capacidad_transporte(self):
        return self.__capacidad_transporte
    
    def set_capacidad_transporte(self, capacidad_transporte):
        self.__capacidad_transporte = capacidad_transporte
        
    def get_peso(self):
        return self.__peso
    
    def set_peso(self, peso):
        self.__peso = peso

    def get_empuje(self):
        return self.__empuje
    
    def set_empuje(self, empuje):
        self.__empuje = empuje

