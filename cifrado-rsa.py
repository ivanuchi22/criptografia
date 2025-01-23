# Configuración parámetros clave pública
e = 17
n = 3233

# Mensaje para cifrar
message = input("Introduzca el mensaje para cifrar: ")

# Definimos la función para cifrar los caracteres
def rsa_encrypt_char(char, e, n):
    m = ord(char)  # Convierte el caracter a su valor ASCII
    c = pow(m, e, n)  # Realiza la operación c = m^e mod n
    return c

# Cifrado del mensaje
ciphertext = [rsa_encrypt_char(char, e, n) for char in message]
for char, c in zip(message, ciphertext):
        print(char, " -> c = ", c)

print("Texto cifrado completo: ", ciphertext)
