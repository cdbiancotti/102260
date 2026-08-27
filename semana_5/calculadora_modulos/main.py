import operaciones

numero_1 = 10
numero_2 = 0

print("Suma:", operaciones.sumar(numero_1, numero_2))
print("Resta:", operaciones.restar(numero_1, numero_2))
print("Multiplicación:", operaciones.multiplicar(numero_1, numero_2))

resultado_division = operaciones.dividir(numero_1, numero_2)


if resultado_division is None:
    print("No se puede dividir por cero.")
else:
    print("División:", resultado_division)
