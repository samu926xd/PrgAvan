import tkinter  as tk 
from tkinter import ttk
from .Manejo_archivoL import *
from .Manejo_archivoA import *
from .Libros import *
from .Autor import *
from tkinter import messagebox 
from tkinter import simpledialog



class Frame(tk.Frame):
    def __init__(self, root=None, Libros=None, Autor=None, cal=None, caa=None, ListLibros=None, ListAutor=None):
        super().__init__(root, width=1240, height=800)
        self.root = root
        self.Libros = Libros
        self.Autor = Autor
        self.cal = cal
        self.caa = caa
        self.ListLibros = ListLibros
        self.ListAutor = ListAutor
        self.pack()
        self.infolibros()
        self.deshabilitar_campos()
        self.tabla_libros()
        self.barra_menu()
        

        
    def infolibros(self):
        
        #titulos de los inputs
        self.label_titulo = tk.Label(self, text="Titulo: ")
        self.label_titulo.config(font=("Arial", 16) , fg="black")
        self.label_titulo.grid(row = 0 , column=0, padx=5, pady=5)
        
        self.label_año = tk.Label(self, text="Año Publicacion: ")
        self.label_año.config(font=("Arial", 16),  fg="black")
        self.label_año.grid(row = 1 , column=0, padx=5, pady=5)
        
        self.label_autor = tk.Label(self, text="Autor: ")
        self.label_autor.config(font=("Arial", 16),  fg="black")
        self.label_autor.grid(row = 2 , column=0, padx=5, pady=5)
        
        self.label_nac = tk.Label(self, text="Nacionalidad: ")
        self.label_nac.config(font=("Arial", 16),  fg="black")
        self.label_nac.grid(row = 3 , column=0, padx=5, pady=5)
        
        self.label_gen = tk.Label(self, text="Genero: ")
        self.label_gen.config(font=("Arial", 16),  fg="black")
        self.label_gen.grid(row = 0 , column=2, padx=5, pady=5)
        
        self.label_cat = tk.Label(self, text="Categoria: ")
        self.label_cat.config(font=("Arial", 16),  fg="black")
        self.label_cat.grid(row = 2 , column=2, padx=5, pady=0)
        

        
        #input en textos
        self.titulo = tk.StringVar()
        self.entry_titulo = tk.Entry(self, textvariable=self.titulo)
        self.entry_titulo.config(width=30,  font=("Arial", 16))
        self.entry_titulo.grid(row=0, column=1, padx=5, pady=5)
        
        self.año = tk.StringVar()
        self.entry_año = tk.Entry(self, textvariable=self.año)
        self.entry_año.config(width=30,  font=("Arial", 16))
        self.entry_año.grid(row=1, column=1,padx=5, pady=5)
        
        self.autor = tk.StringVar()
        self.entry_autor = tk.Entry(self, textvariable=self.autor)
        self.entry_autor.config(width=30,  font=("Arial", 16))
        self.entry_autor.grid(row=2, column=1, padx=5, pady=5)
        
        self.nac = tk.StringVar()
        self.entry_nac = tk.Entry(self, textvariable=self.nac)
        self.entry_nac.config(width=30,  font=("Arial", 16))
        self.entry_nac.grid(row=3, column=1, padx=5, pady=5)
        
        self.gen = tk.StringVar()
        self.entry_gen = tk.Entry(self, textvariable=self.gen)
        self.entry_gen.config(width=30,  font=("Arial", 16))
        self.entry_gen.grid(row=0, column=3, padx=5, pady=5)
        
        
        
        #Botones 
        self.boton_ingresar = tk.Button(self, text="Ingresar", command=self.habilitar_campos)
        self.boton_ingresar.config(width=20,font=("Arial", 16), bg="blue", fg="white", cursor="hand2")
        self.boton_ingresar.grid(row=4, column=0, padx=10, pady=10)
        
        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_libro)
        self.boton_guardar.config(width=20,font=("Arial", 16), bg="green", fg="white", cursor="hand2")
        self.boton_guardar.grid(row=4, column=1, padx=10, pady=10)
        
        self.boton_buscar = tk.Button(self, text="Buscar", command=self.mostrar_ventana_busqueda)
        self.boton_buscar.config(width=20,font=("Arial", 16), bg="yellow", fg="black", cursor="hand2")
        self.boton_buscar.grid(row=4, column=2, padx=10, pady=10)
        
        self.boton_cancelar = tk.Button(self, text="Cancelar", command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20,font=("Arial", 16), bg="red", fg="white", cursor="hand2")
        self.boton_cancelar.grid(row=4, column=3, padx=10, pady=10)
        
        #botones inferiores
        self.boton_modificar = tk.Button(self, text="Modificar",command=self.mostrar_ventana_modificacion)
        self.boton_modificar.config(width=20,font=("Arial", 16), bg="yellow", fg="black", cursor="hand2")
        self.boton_modificar.grid(row=7, column=1, padx=10, pady=10)
        
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.mostrar_ventana_eliminacion)
        self.boton_eliminar.config(width=20,font=("Arial", 16), bg="red", fg="black", cursor="hand2")
        self.boton_eliminar.grid(row=7, column=2, padx=10, pady=10)
        
        #radio boton 
        
        self.selected_option = tk.StringVar()
        self.selected_option.set(" ")

        self.radio_a = tk.Radiobutton(self, text="Ciencia ", value="ciencia", variable=self.selected_option, command= lambda: print(f"Selected: {self.selected_option.get()}"))
        self.radio_a .config(width=5,font=("Arial",12), fg="black")
        self.radio_a.grid(row=1, column=3, padx=1, pady=1)
        
        self.radio_a = tk.Radiobutton(self, text="Novela ", value="novela", variable=self.selected_option, command= lambda: print(f"Selected: {self.selected_option.get()}"))
        self.radio_a .config(width=5,font=("Arial",12), fg="black")
        self.radio_a.grid(row=2, column=3, padx=1, pady=1)
        
        self.radio_a = tk.Radiobutton(self, text="Historia ", value="historia", variable=self.selected_option, command= lambda: print(f"Selected: {self.selected_option.get()}"))
        self.radio_a .config(width=5,font=("Arial",12), fg="black")
        self.radio_a.grid(row=3, column=3, padx=1, pady=1)
        
    #barra para salir   
    def barra_menu(self):
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu, width=1240, height=800)
        
        menu_inicio = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
        menu_inicio.add_command(label="Salir", command=self.root.destroy)   
        
        
        
    def habilitar_campos(self):
        self.entry_titulo.config(state="normal")
        self.entry_año.config(state="normal")
        self.entry_autor.config(state="normal")
        self.entry_nac.config(state="normal")
        self.entry_gen.config(state="normal")
        self.boton_guardar.config(state="normal")
        self.boton_buscar.config(state="normal")
        
        
        
    def deshabilitar_campos(self):
        self.titulo.set("")
        self.año.set("")
        self.autor.set("")
        self.nac.set("")
        self.gen.set("")
        self.entry_titulo.config(state="disabled")
        self.entry_año.config(state="disabled")
        self.entry_autor.config(state="disabled")
        self.entry_nac.config(state="disabled")
        self.entry_gen.config(state="disabled")
        self.boton_guardar.config(state="disabled")
        self.boton_buscar.config(state="disabled")
        
    def guardar_libro(self):
        titulo = self.titulo.get()
        año = self.año.get()
        autor = self.autor.get()
        nac =self.nac.get()
        gen =self.gen.get()
        cat=self.selected_option.get() 
        
        nuevo_id = str(len(self.Libros) + 1)
        
        self.Libros[nuevo_id] = {"Titulo": titulo, "Año": año}
        self.cal.Guardar(self.Libros)
        self.Autor[nuevo_id] = {"Nombre": autor, "Nacionalidad": nac}
        self.caa.Guardar(self.Autor)
        self.tabla.insert('', 'end', text=nuevo_id, values=(titulo, año, autor, nac, gen, cat))
        self.deshabilitar_campos()
        

    def tabla_libros(self):
        self.tabla = ttk.Treeview(self, columns=("Titulo", "Año", "Autor", "Nacionalidad","Genero","Categoria"), show="headings")
        self.tabla.grid(row=5, column=0, columnspan=7, padx=5, pady=5)
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("Titulo", text="Titulo")
        self.tabla.heading("Año", text="Año")
        self.tabla.heading("Autor", text="Autor")
        self.tabla.heading("Nacionalidad", text="Nacionalidad")
        self.tabla.heading("Genero", text="Genero")
        self.tabla.heading("Categoria", text="Categoria")
        
        
        for clave in self.Libros.keys():
            titulo = self.Libros[clave].get("Titulo", "")
            año = self.Libros[clave].get("Año", "")
            nombre_autor = self.Autor.get(clave, {}).get("Nombre", "")
            nac = self.Autor.get(clave, {}).get("Nacionalidad", "")
            self.tabla.insert('', 'end', text=clave, values=(titulo, año, nombre_autor, nac))
    
    def buscar_libro(self):
        codigo = self.entry_codigo.get()
        if codigo in self.Libros:
            libro = self.Libros[codigo]
            self.titulo.set(libro.get("Titulo", ""))
            self.año.set(libro.get("Año", ""))
            autor_info = self.Autor.get(codigo, {})
            self.autor.set(autor_info.get("Nombre", ""))
            self.nac.set(autor_info.get("Nacionalidad", ""))
        else:
            tk.messagebox.showerror("Error", "Libro no encontrado")     
    
    def mostrar_ventana_busqueda(self):
        ventana = tk.Toplevel(self)
        ventana.title("Buscar libro por código")
        ventana.geometry("400x200")
        label_codigo = tk.Label(ventana, text="Ingrese código del libro:", font=("Arial", 14))
        label_codigo.pack(pady=10)
        self.entry_codigo = tk.Entry(ventana, font=("Arial", 14))
        self.entry_codigo.pack(pady=10)
        boton_buscar = tk.Button(
        ventana, text="Buscar", font=("Arial", 14), bg="green", fg="white",
        command=lambda: [self.buscar_libro(), ventana.destroy()])
        boton_buscar.pack(pady=10)     
    
    def modificar_libro(self, codigo):
        if codigo in self.Libros:
            titulo = self.titulo.get()
            año = self.año.get()
            autor = self.autor.get()
            nac = self.nac.get()
            gen =self.gen.get()
            cat=self.selected_option.get() 
            self.Libros[codigo] = {"Titulo": titulo, "Año": año}
            self.cal.Guardar(self.Libros)
            self.Autor[codigo] = {"Nombre": autor, "Nacionalidad": nac}
            self.caa.Guardar(self.Autor)
            for item in self.tabla.get_children():
                if self.tabla.item(item, "text") == codigo:
                    self.tabla.item(item, values=(titulo, año, autor, nac, gen, cat))
                    break
            tk.messagebox.showinfo("Modificado", "Los datos fueron actualizados correctamente.")
        else:
            tk.messagebox.showerror("Error", "Código de libro no encontrado.")

    def mostrar_ventana_modificacion(self):
        ventana = tk.Toplevel(self)
        ventana.title("Modificar libro por código")
        ventana.geometry("400x200")

        label_codigo = tk.Label(ventana, text="Ingrese código del libro:", font=("Arial", 14))
        label_codigo.pack(pady=10)

        entry_codigo = tk.Entry(ventana, font=("Arial", 14))
        entry_codigo.pack(pady=10)

        def ejecutar_modificacion():
            codigo = entry_codigo.get()
            self.modificar_libro(codigo)
            ventana.destroy()

        boton_modificar = tk.Button(
            ventana,
            text="Modificar",
            font=("Arial", 14),
            bg="purple",
            fg="white",
            command=ejecutar_modificacion)
        boton_modificar.pack(pady=10)
    
    def eliminar_libro(self, codigo):
        if codigo in self.Libros:
            del self.Libros[codigo]
            del self.Autor[codigo]
            self.cal.Guardar(self.Libros)
            self.caa.Guardar(self.Autor)
            for item in self.tabla.get_children():
                if self.tabla.item(item, "text") == codigo:
                    self.tabla.delete(item)
                    break
            tk.messagebox.showinfo("Eliminado", "El libro ha sido eliminado correctamente.")
        else:
            tk.messagebox.showerror("Error", "Código de libro no encontrado.")
        
    def mostrar_ventana_eliminacion(self):
        ventana = tk.Toplevel(self)
        ventana.title("Eliminar libro por código")
        ventana.geometry("400x200")
        label = tk.Label(ventana, text="Ingrese código del libro:", font=("Arial", 14))
        label.pack(pady=10)
        entry_codigo = tk.Entry(ventana, font=("Arial", 14))
        entry_codigo.pack(pady=10)
        
        def ejecutar_eliminacion():
            codigo = entry_codigo.get()
            self.eliminar_libro(codigo)
            ventana.destroy()
        
        boton = tk.Button(
            ventana, text="Eliminar", font=("Arial", 14), bg="red", fg="white",
            command= ejecutar_eliminacion)
        boton.pack(pady=10)
    
            