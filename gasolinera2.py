totalLitros = 0 # acumulador para los litros vendidos
while totalLitros <= 100:
    venta = float(input("ingrese los litrosvendidos: "))
    totalLitros += venta 

    if totalLitros < 100:
        print("sigue vendiendo")
    else:
        print("meta diaria alcanzada")