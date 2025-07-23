from .Manejo_archivoA import *
class ControlAutor:
    def __init__(self):
        self.__nombre:str=''
        self.__nac:str=''
    

    @property
    def nombre(self)->str:
        return self.__nombre
    @nombre.setter
    def nombre(self, new_value:str):
        self.__nombre = new_value
    
    @property
    def nac(self)->str:
        return self.__nac
    @nac.setter
    def nac(self, new_value:str):
        self.__nac = new_value

    def ModificarAutor(self,info:dict,dataTemp:dict,archivo:str):
        diccb=dataTemp.get(info,-1)
        if(diccb == -1):
            print("El codigo no existe")
        else:
            diccb['nac'] = input("Ingrese correccion de la nacionalidad: ")
            dataTemp.update({info: diccb})
            archivoM = ControlArchivoA(archivo,dataTemp)
            archivoM.Editar(dataTemp)
            print(dataTemp)
            
    def CrearAutor(self,info:dict,archivo:str):
        archivoM = ControlArchivoA(archivo,info)
        nombre = input("Ingrese el  nombre del autor: ")
        nac = input("Ingrese nacionalidad del autor: ")
        ListAutor={
            "nombre": nombre,
            "nac": nac  
        }
        info.update({str(len(info)+1).zfill(4): ListAutor})
        archivoM.Guardar(info)  
    
    def MostrarAutor(self,info: dict):
        pass
    
        