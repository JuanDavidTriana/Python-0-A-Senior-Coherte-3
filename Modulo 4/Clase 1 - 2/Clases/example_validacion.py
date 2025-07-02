def agregar_usuario(nombre,edad,email):
    usuarios = []

    if not nombre:
        # raise Exception("Error, el nombre no puede estar vacio")
        print("Error, el nombre no puede estar vacio")
        return
    
    elif len(nombre) > 60:
        print("Error, no puede ser mayor a 60 caracteres")
        return

    if not edad.isdigit():
        print("Error, La edad debe ser un numero entero")
        return
    
    elif int(edad) <=0:
        print("Error, La edad debe ser un numero positivo")
        return
    
    elif int (edad) > 150:
        print("Error, entrar enntre un rango de edad")
        return
        
        
    if '@' not in email or "." not in email:
        print("Error: el email no es valido")
        return

    nuevo_usuario = {
        "nombre": nombre,
        "edad": edad,
        "email": email
    }

    usuarios.append(nuevo_usuario)

    print(usuarios)

nombre = input("Nombre del usuario: ")
edad = input("Edad del usuario: ")
email = input("Email del usuario: ")

agregar_usuario(nombre,edad, email)
