sueldo = float(input("Ingrese el sueldo de empleado recibido: "))
bono = 0

if sueldo > 3000:
    bono = sueldo * 0.1 
    print("El bono que recibira sera del 10%")
elif sueldo> 1500 and sueldo <= 2999:
    bono = sueldo * 0.05
    print("El bono que recibira sera del 5%")
elif sueldo <= 1499:
    print("No recibira bono")