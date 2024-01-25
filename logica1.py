# Solicitar al usuario que ingrese los tres números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))


mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)
centro = num1 + num2 + num3 - mayor - menor


print("Números en orden de mayor a menor:", mayor, centro, menor)


print("Números en orden de menor a mayor:", menor, centro, mayor)

# Verifica si los números son iguales
if num1 == num2 == num3:
    print("Los números son iguales.")
