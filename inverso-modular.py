# Parámetros
e = int(input("Introduzca el valor de e: "))
phi_n = int(input("Introduzca el valor de phi_n: "))

# Cálculo del inverso modular
d = pow(e, -1, phi_n)

print("El valor de d es: ", d)
