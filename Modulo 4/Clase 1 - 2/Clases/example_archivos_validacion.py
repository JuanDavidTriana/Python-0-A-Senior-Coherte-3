
class Control:
    def __init__(self):
        self.usuarios = []
        self.cargar_datos()

    def cargar_datos(self):
        
        with open("info/usuarios.txt", "r") as archivo:
            contenido = archivo.read()
            if contenido: 
                usuarios = contenido.split(';')
                self.usuarios = [u for u in usuarios if u]
            else:
                print("No hay cantenido de cargar")
    def exportar_txt():
        global usuarios

        with open('info/usuarios.txt','w') as archivo:
            archivo.write(';'.join(usuarios))

        print("Usuario guardado")

    def ver_usuarios(self):

        if not self.usuarios:
            print("No hay usuarios par mostrar")

        for usuario in self.usuarios:
            print(f"- {usuario}")

    def cargar_usuarios(self):

        nombre = input("Digite un nombre: ").lower()

        if ';' in nombre :
            print("Error: el nombre no puede llevar ;")
            return    
        
        if not nombre:
            print("Error: el nombre no puede estar vacio")
            return

        if len(nombre) > 60:
            print("Error: el nombre no puede tener mas de 60 carcteres")
            return
        
        self.usuarios.append(nombre)

        print("Usuarios agregado exitosamente")

control = Control()

while True:
    
    print("1. Agregar")
    print("2. Ver")
    print("0. Salir")

    opcion = input("Digite un opcion: ")

    match opcion:
        case '1':
            control.cargar_usuarios()
        case '2':
            control.ver_usuarios()
        case '0':
            print("Finalizando")
            control.exportar_txt()
            break
        case _:
            print("Opcion no valida")
    