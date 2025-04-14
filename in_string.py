def check_vowels():
 # Código a implementar utilizando input.
    # Solicito un nombre y lo paso a minúsculas para facilitar el reconocimiento de las vocales:
    nombre = input("Ingrese un nombre: ")
    nombre = nombre.lower()

# "Verificador" de vocales:
    print("Contiene a:", "a" in nombre)
    print("Contiene e:", "e" in nombre)
    print("Contiene i:", "i" in nombre)
    print("Contiene o:", "o" in nombre)
    print("Contiene u:", "u" in nombre)

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
