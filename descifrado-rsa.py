# Configuración parámetros clave privada
d = 2753
n = 3233

# Mensaje para descifrar
ciphertext = [3000, 1307, 2726, 2790, 1992, 3123, 2310, 3165, 1759, 1307]

# Definimos la función para descifrar los caracteres
def rsa_decrypt_char(c, d, n):
    m = pow(c, d, n)  # Realizar la operación c^d mod n
    return chr(m)  # Convertir el valor numérico al carácter original

# Descifrado de mensaje
plaintext = ''.join(rsa_decrypt_char(c, d, n) for c in ciphertext)
for char, c in zip(ciphertext, plaintext):
        print(char, " -> c = ", c)

print("Texto descifrado: ", plaintext)
