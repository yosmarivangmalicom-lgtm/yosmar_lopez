try:
    num1 = int(input("Ingresa un número: "))
    num2 = int(input("Ingresa otro número: "))
    
    resultado = num1 / num2
    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")

except ValueError:
    print("Error: Debes ingresar números válidos")