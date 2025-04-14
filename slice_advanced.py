def slice_advanced():
 # Código a implementar utilizando input.
    # Defino el texto en cuestión:
    txt = "awesome"

    # Printeo sus distintas secciones:

    #  0   1   2   3   4   5   6
    # (a   w   e   s   o   m   e)
    # -7  -6  -5  -4  -3  -2  -1

    print(txt[:4]) 
    print(txt[2:5])
    print(txt[:])

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`
