capital_inicial = int(input("Ingrese el capital inicial: "))
interes_anual = int(input("Ingrese la tasa de interes anual: "))
cantidad_años = int(input("Ingrese la cantidad de años: "))
decimal = interes_anual / 100
valor = (1 + decimal)**cantidad_años
monto_final = valor * capital_inicial
interes_ganado = monto_final - capital_inicial

print(f"""Capital inicial: {capital_inicial:>3}
Tasa: {interes_anual}
Años: {cantidad_años}""")
print("El monto final es de: ", monto_final )
print("El interes ganado es de: ", interes_ganado)