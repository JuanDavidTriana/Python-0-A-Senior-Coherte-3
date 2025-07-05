from datetime import datetime

class Libro:
    def __init__(self, codigo:str,titulo:str, autor:str, stock:int = 1):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.stock = stock

    @classmethod
    def from_string(cls, linea: str) -> 'Libro':
        datos = linea.strip().split('|')
        return cls(datos[0],datos[1],datos[2],datos[3])

    def to_string(self) -> str:
        return f"{self.codigo}|{self.titulo}|{self.autor}|{self.stock}"
    
    def __str__(self):
        return f"{self.titulo} por {self.autor} (stock: {self.stock})"

class Usuario:
    def __init__(self,codigo,nombre, email):
        self.codigo = codigo
        self.nombre = nombre 
        self.email = email

class Prestamo:
    def __init__(self, codigo_libro:str, codigo_usuario:str):
        self.codigo_libro = codigo_libro
        self.codigo_usuario = codigo_usuario
        self.fecha_prestamos = datetime.now().strftime("%Y-%m-%d")
