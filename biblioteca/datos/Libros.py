from .Manejo_archivoL import *

class ControlLibros:
    def __init__(self):
        self.__titulo:str=''
        self.__año:int = 0
    

    @property
    def titulo(self)->str:
        return self.__titulo
    @titulo.setter
    def titulo(self, new_value:str):
        self.__titulo = new_value
    
    @property
    def año(self)->int:
        return self.__año
    @año.setter
    def año(self, new_value:int):
        self.__año = new_value

    def ModificarLibro(self,info:dict,dataTemp:dict,archivo:str):  
        diccb=dataTemp.get(info,-1)
        if(diccb == -1):
            print("El codigo no existe")
        else:
            diccb['año'] = int(input("Ingrese correccion del año: "))
            dataTemp.update({info: diccb})
            archivoM = ControlArchivoL(archivo,dataTemp)
            archivoM.Editar(dataTemp)
            print(dataTemp)
      
    def CrearLibro(self,info:dict,archivo:str):
        archivoM = ControlArchivoL(archivo,info)
        titulo = input("Ingrese  el titulo del libro: ")
        año = int(input("Ingrese año de publicacion del libro: "))
        ListLibros={
            "titulo": titulo,
            "año": año  
        }
        info.update({str(len(info)+1).zfill(4): ListLibros})
        archivoM.Guardar(info)  
    
    def MostrarLibro(self,info: dict):
        pass
     
        