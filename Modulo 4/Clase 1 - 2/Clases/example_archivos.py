usuarios = []

def exportar_txt():
    global usuarios

    with open('usuarios.txt','w') as archivo:
        archivo.write(';'.join(usuarios))

 

    print("Usuario guardado")

def ver_usuarios():
    global usuarios

    if not usuarios:
        print("No hay usuarios par mostrar")

    for usuario in usuarios:
        print(f"- {usuario}")

def cargar_datos():
    global usuarios
    
    with open("usuarios.txt", "r") as archivo:
        contenido = archivo.read()
        if contenido: 
            usuarios = contenido.split(';')
            usuarios = [u for u in usuarios if u]
        else:
            print("No hay cantenido de cargar")
  
    
def cargar_usuarios():
    global usuarios

    nombre = input("Digite un nombre: ").lower()

    if ';' in nombre :
        print("Error: el nombre no puede llevar ;")
        return    

    usuarios.append(nombre)

    print("Usuarios agregado exitosamente")

cargar_datos()
while True:
    
    print("1. Agregar")
    print("2. Ver")
    print("0. Salir")

    opcion = input("Digite un opcion: ")

    match opcion:
        case '1':
            cargar_usuarios()
        case '2':
            ver_usuarios()
        case '0':
            print("Finalizando")
            exportar_txt()
            break
        case _:
            print("Opcion no valida")
    