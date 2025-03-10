def factorial(n):$
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    return 1 if n == 0 else n * factorial(n - 1)

num = int(input("Ingrese un número entero: "))
print(f"El factorial de {num} es {factorial(num)}")
