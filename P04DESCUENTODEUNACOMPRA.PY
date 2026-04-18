total = float(input("Total de la compra: "))
cliente_frecuente = input("¿Eres cliente frecuente? (si/no): ")

if (total > 1000 and cliente_frecuente == "si") or not (total < 500):
    descuento = total * 0.10
    print("Tienes descuento de:", descuento)
else:
    print("No tienes descuento")