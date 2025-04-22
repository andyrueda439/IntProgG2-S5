edad = int(input("Ingrese la edad de una persona: "))
edad_valida = 18

if edad > edad_valida:
    print("Puede votar")
else: print("No puede votar por ser menor de edad")