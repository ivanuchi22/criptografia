# Parámetro n interceptado de la clave pública
n = 3233

# Definimos la función que factoriza n
def factorize_n(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None, None

# Factorización
p, q = factorize_n(n)
print("p = ",p)
print("q = ",q)
