
palabras_clave = [
    "a", "ante", "bajo", "con", "contra", "de", "desde", "en", "entre", "hacia", "hasta", "para", "por", "según", "sin", "so", "sobre", "tras",
    "cifrado", "descifrar", "clave", "criptografía", "encriptado", "mensaje", 
    "seguridad", "encriptación", "algoritmo", "criptoanalista", "contraseña", "cifrador", 
    "criptoanálisis", "ciberseguridad", "criptoanálisis", "ataque", "seguro", "hacker", "firewall", "vulnerabilidad", "protección", 
    "cifrado simétrico", "cifrado asimétrico", "RSA", "AES", "DES", "seguridad informática", "hash", "SSL", "TLS", "autenticación", "seguridad de red"
]

mensaje_encriptado = "dv xawwmkzypjdvvv wn hmxzj hsn lmz pfv xmzkoajf vz dfagmevlduv"

def descifrar_cesar(texto, clave_n, clave_m):
    resultado = ""
    for i, letra in enumerate(texto):
        if letra == ' ':
            resultado += ' '
        else:
            if i % 2 == 0:
                # Desplazar con clave_n
                offset = (ord(letra) - ord('a') - clave_n) % 26
            else:
                # Desplazar con clave_m
                offset = (ord(letra) - ord('a') - clave_m) % 26
            resultado += chr(ord('a') + offset)
    return resultado

# Variables para mantener el mejor resultado
mejor_mensaje = ""
mejor_claves = ""
mejor_palabras_clave = []

# Iterar a través de todas las combinaciones posibles de claves de desplazamiento
for clave_n in range(1, 27):
    for clave_m in range(1, 27):
        mensaje_descifrado = descifrar_cesar(mensaje_encriptado, clave_n, clave_m)
        palabras_encontradas = [palabra for palabra in palabras_clave if palabra in mensaje_descifrado]
        if palabras_encontradas:
            # Si se encuentra una combinación con palabras clave, actualiza el mejor resultado
            if len(palabras_encontradas) > len(mejor_palabras_clave):
                mejor_mensaje = mensaje_descifrado
                mejor_claves = f"{clave_n}-{clave_m}"
                mejor_palabras_clave = palabras_encontradas

# Imprimir el mejor resultado encontrado
if mejor_mensaje:
    print(f"Mejor combinación de claves: {mejor_claves}")
    print(f"Mensaje descifrado: {mejor_mensaje}")
    print(f"Palabras clave encontradas: {mejor_palabras_clave}")
else:
    print("No se encontró un mensaje significativo con las palabras clave proporcionadas.")
