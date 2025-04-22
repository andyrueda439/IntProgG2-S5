litros_mes = int(input("Ingrese la cantidad de litros consumidos en un  mes en una vivienda: "))
personas_casa = int( input("Ingrese la camtidad de personas que habitan en la casa: "))
consumo_mensual_persona = litros_mes / personas_casa
consumo_diario_persona = consumo_mensual_persona / 30

print(f"""Litros consumidos: {litros_mes}
Personas que habitan: {personas_casa}
Consumo mensual por persona: {consumo_mensual_persona}
consumo diario por persona: {consumo_diario_persona}""")