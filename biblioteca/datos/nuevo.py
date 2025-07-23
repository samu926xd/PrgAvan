# este es una copia de guiclie pero intentando anidar las funciones 

import tkinter  as tk 
from tkinter import ttk
from Manejo_archivoA import* 
from Manejo_archivoL import * 
from Libros import * 
from Autor import * 
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


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root,width=480, height=320)
        self.root = root
        self.pack()
        #self.config( bg="grey")
        
        self.infolibros()
        self.deshabilitar_campos()
        self.tabla_libros()
        
        
        
    def infolibros(self):
        
        #titulos de los inputs
        self.label_titulo = tk.Label(self, text="Titulo: ")
        self.label_titulo.config(font=("Arial", 16) , fg="black")
        self.label_titulo.grid(row = 0 , column=0, padx=10, pady=10)
        
        self.label_autor = tk.Label(self, text="Autor: ")
        self.label_autor.config(font=("Arial", 16),  fg="black")
        self.label_autor.grid(row = 1 , column=0, padx=10, pady=10)
        
        
        #input en textos
        self.titulo = tk.StringVar()
        self.entry_titulo = tk.Entry(self, textvariable=self.titulo)
        self.entry_titulo.config(width=50,  font=("Arial", 16))
        self.entry_titulo.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        
        self.autor = tk.StringVar()
        self.entry_autor = tk.Entry(self, textvariable=self.autor)
        self.entry_autor.config(width=50, font=("Arial", 16))
        self.entry_autor.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        
        #Botones 
        self.boton_ingresar = tk.Button(self, text="Ingresar", command=self.habilitar_campos)
        self.boton_ingresar.config(width=20,font=("Arial", 16), bg="blue", fg="white", cursor="hand2")
        self.boton_ingresar.grid(row=2, column=0, padx=10, pady=10)
        
        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_libro)
        self.boton_guardar.config(width=20,font=("Arial", 16), bg="green", fg="white", cursor="hand2")
        self.boton_guardar.grid(row=2, column=1, padx=10, pady=10)
        
        self.boton_buscar = tk.Button(self, text="Buscar")
        self.boton_buscar.config(width=20,font=("Arial", 16), bg="yellow", fg="black", cursor="hand2")
        self.boton_buscar.grid(row=2, column=2, padx=10, pady=10)
        
        self.boton_cancelar = tk.Button(self, text="Cancelar", command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20,font=("Arial", 16), bg="red", fg="white", cursor="hand2")
        self.boton_cancelar.grid(row=2, column=3, padx=10, pady=10)
        
        
    def habilitar_campos(self):
        self.entry_titulo.config(state="normal")
        self.entry_autor.config(state="normal")
        self.boton_guardar.config(state="normal")
        self.boton_buscar.config(state="normal")
        
        
        
    def deshabilitar_campos(self):
        self.titulo.set("")
        self.autor.set("")
        self.entry_titulo.config(state="disabled")
        self.entry_autor.config(state="disabled")
        self.boton_guardar.config(state="disabled")
        self.boton_buscar.config(state="disabled")
        
    def guardar_libro(self):
        self.deshabilitar_campos()
        ListLibros.CrearLibro(Libros,cal.archivo)
        ListAutor.CrearAutor(Autor,caa.archivo)

    def tabla_libros(self):
        self.tabla = ttk.Treeview(self, column =("Titulo", "Autor"))
        self.tabla.grid(row=3, column=0, columnspan=4, padx=10, pady=10)
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Titulo")
        self.tabla.heading("#2", text="Autor")
            