# Crea un diccionario llamado "frutas" con las siguientes parejas clave-valor:
frutas = {
    "manzana" : "roja",
    "banana" :"amarilla",
    "pera" : "verde",
    "naranja" : "naranja"
}
       
# Imprime el diccionario "frutas" en la consola.
for clave, valor in frutas.items():
    print(clave, valor)


# Imprime el valor asociado a la clave "banana" en la consola.
print(frutas["banana"])  # amarilla

# Imprime el valor asociado a la clave "uva" en la consola.
print(frutas.get("uva"))
