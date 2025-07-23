import tkinter as tk
from biblioteca.datos.guiclie import Frame
from biblioteca.datos.Manejo_archivoL import ControlArchivoL
from biblioteca.datos.Manejo_archivoA import ControlArchivoA
from biblioteca.datos.Libros import ControlLibros
from biblioteca.datos.Autor import ControlAutor

Libros = {}
Autor = {}

cal = ControlArchivoL("Libros.json", Libros)
caa = ControlArchivoA("Autor.json", Autor)

if cal.checkFile():
    Libros = cal.Cargar()
    Autor = caa.Cargar()
else:
    cal.Guardar(Libros)
    cal.Guardar(Autor)

if caa.checkFile():
    Autor = caa.Cargar()
    Libros = cal.Cargar()
else:
    caa.Guardar(Autor)
    cal.Guardar(Libros)

ListLibros = ControlLibros()
ListAutor = ControlAutor()

root = tk.Tk()
root.title("Biblioteca S6")
root.iconbitmap("biblioteca/img/icolib.ico")
app = Frame(root, Libros=Libros, Autor=Autor, cal=cal, caa=caa, ListLibros=ListLibros, ListAutor=ListAutor)
app.mainloop()
