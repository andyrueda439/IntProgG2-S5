distancia_kilometros = int(input("Ingrese la distancia recorrida: "))
litros_consumidos = int(input("Ingrese la cantidad de litros consumidos: "))
precio = 36.80
rendimiento = distancia_kilometros / litros_consumidos
gasto_total = litros_consumidos * precio

print(f"""Kilometros: {distancia_kilometros:>3}
Litros de combustible: {litros_consumidos:>3}
Precio: {precio:>3}""")
print("El rendimiento total del vehiculo es de: ", rendimiento)
print("El gasto total del combustible: ", gasto_total)