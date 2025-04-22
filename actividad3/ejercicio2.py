cantidad_inicial = int(input("Ingresar la cantidad inicial: "))
cantidad_recibidos = int(input("Ingresar la cantidad de productos recibidos: "))
cantidad_vendidos = int(input("Ingresar la cantidad de productos vendidos: "))
suma = cantidad_recibidos + cantidad_inicial
resta = suma - cantidad_vendidos

print(f"""Cantidad inicial: {cantidad_inicial:>3}
Cantidad recibidos: {cantidad_recibidos:>3}
Cantidad vendidos : {cantidad_vendidos:>3}
{"Inventario final":<15}{resta:>3.0f}""")
print("El inventario final es de: ", resta)