texto = "  Python es divertido  "

texto.strip()
texto.upper()
texto.lower()
len(texto)
if "Python" in texto:
   print("Texto contiene la palabra Python")
else:
    print("Texto no contiene la palabra Python")

texto2 = texto.replace("divertido", "poderoso")
print(texto2)
