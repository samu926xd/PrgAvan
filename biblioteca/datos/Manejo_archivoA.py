import json 

class ControlArchivoA:
    def __init__(self, archivo:str, info:dict):
        self.__archivo = archivo
        self.__infodata = info    
    
    @property
    def archivo(self):
        return self.__archivo 
    
    @archivo.setter
    def archivo(self, new_value:dict):
        self.__archivo = new_value   
    
    @property
    def infodata(self):
        return self.__infodata  
    
    @infodata.setter
    def infodata(self, new_value:dict):
        self.__infodata = new_value      
    
    def Guardar(self,info:dict):
        with open('biblioteca/datos/'+self.__archivo, "w") as write_file: 
            json.dump(info, write_file,indent=4)
            write_file.close()
    
    def Editar(self,info:dict):
        with open('biblioteca/datos/'+self.__archivo, "r+") as file:
            dataTemp =json.load(file)
            file.seek(0)    
            json.dump(info, file, indent=4)
            file.close()       
    
    def Cargar(self):            
        with open('biblioteca/datos/'+self.__archivo, "r") as read_file:
            info = json.load(read_file)  
        return info  
    
    def Borrar(self, info:dict,llave:str):
        self.__infodata.pop(llave)
        self.Guardar(self.__infodata)
    
    def checkFile(self) -> bool:
        try:
            with open('biblioteca/datos/'+self.__archivo,'r') as f:
                return True
        except FileNotFoundError as e:
            return False
        except IOError as e:
            return False    

            
            