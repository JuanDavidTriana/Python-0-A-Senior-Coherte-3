
'''
while True:
    x = 5

    try:
        y = int(input("Digite un numero que no sea 0: "))
        print(x/y)
    except ZeroDivisionError as e:
        print("No se puede divir entre 0")

'''

'''
while True:
    x = 5

    
    y = int(input("Digite un numero que no sea 0: "))
    if not y == 0: # Si y es diferente a 0
        print(x/y)

'''

x = 5

try:

    y = int(input("Digite un numero que no sea 0: "))

    if y == 0:
        raise Exception("El numero no puede ser 0")
    print(x/y)

except ValueError as e:
    print(f"Error: debe digitar un numero {e}")

except Exception as e:
    print(f"Ocurrio un error {e}")

finally:
    print("Muchas gracias por elegirnos")
