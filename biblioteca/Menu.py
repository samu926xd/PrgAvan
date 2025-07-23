from datos.Manejo_archivoA import*
from datos.Manejo_archivoL import *
from datos.Libros import *
from datos.Autor import *
Libros={}
Autor={}

if __name__ == "__main__":
    cal=ControlArchivoL("Libros.json", Libros)
    caa=ControlArchivoA("Autor.json", Autor)
    if cal.checkFile():
        Libros = cal.Cargar()
    else:
        cal.Guardar(Libros)    
    ListLibros = ControlLibros()
    
    if caa.checkFile():
        Autor = caa.Cargar()
    else:
        caa.Guardar(Autor)    
    ListAutor = ControlAutor()
    
    while True:
        print("\nBienvenidos Biblioteca - S6")
        print("\nIngresa una opcion: ")
        print("1. Ingresar Libro/Autor")
        print("2. Modificar Libro/Autor")
        print("3. Mostrar informacion")
        print("4. Eliminar Libro/Autor")
        print("5. Salir")
        menu = input("\nIngrese una opcion: ")
        
        if menu == '1':
            ListLibros.CrearLibro(Libros,cal.archivo)
            ListAutor.CrearAutor(Autor,caa.archivo)
       
        elif menu == '2':
            codM=input("Ingrese codigo del Libro/Autor: ")
            ListLibros.ModificarLibro(codM,Libros,cal.archivo)
            ListAutor.ModificarAutor(codM,Autor,caa.archivo)
       
        elif menu == '3':
            codM = input("Ingrese código del Libro/Autor a mostrar: ")
            if codM in Libros:
                libro = Libros[codM]
                print("\nInformación del Libro:")
                for clave, valor in libro.items():
                    print(f"{clave}: {valor}")
            else:
                print("Código de libro no encontrado.")
            if codM in Autor:
                autor = Autor[codM]
                print("\nInformación del Autor:")
                for clave, valor in autor.items():
                    print(f"{clave}: {valor}")
            else:
                print("Código de autor no encontrado.")
        
        elif menu == '4': 
            codM=input("Ingrese codigo del libro/Autor a eliminar: ")
            cal.infodata = Libros
            caa.infodata = Autor
            cal.Borrar(cal.infodata, codM)
            caa.Borrar(caa.infodata, codM)       
        else:
            print("Saliendo del sistema...")
            break 
        
            