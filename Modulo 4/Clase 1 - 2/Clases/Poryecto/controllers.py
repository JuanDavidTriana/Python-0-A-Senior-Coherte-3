from models import Libro, Usuario, Prestamo
from typing import List

class ControladorLibros:
    
    def __init__(self):
        self.libros = [] #Esto es una lista de libros()
        self._cargar_libros()
    
    def _cargar_libros(self):
        '''Cargar lis libros desde un archivo'''
        try:
            with open("libros.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    if linea.strip():
                        self.libros.append(Libro.from_string(linea))
        except Exception as e:
            print(e)
            return False 
        
    def _guardar_libro(self):
        with open("libros.txt", "w", encoding="utf-8") as f:
            for libro in self.libros:
                f.write(libro.to_string() + "\n")

    def agregar_libro(self, codigo:str, titulo:str, autor:str, stock: int = 1) -> bool:

        libro = Libro(codigo,titulo,autor,stock)
        self.libros.append(libro)
        self._guardar_libro()
        print("Libro creado")
        return True
    
    def listar_libros(self) ->List[Libro]:
        return self.libros


class ControladorUsuarios:
    pass

class ControlladorPrestamo:
    pass

libroContro = ControladorLibros()
#libroContro.agregar_libro("2","Cien Años de Soledad", "Gabriel Garcia", 50)
for i in libroContro.listar_libros():
    print(i)