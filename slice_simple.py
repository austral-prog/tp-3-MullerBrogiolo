def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.

    #Reescribo la palabra en minusculas para facilitar el proceso:
    texto = "Awesome".lower()
    
    # Printeo sus distintas secciones:

    #  0   1   2   3   4   5   6
    # (a   w   e   s   o   m   e)
    # -7  -6  -5  -4  -3  -2  -1

    print(texto[0:3])
    print(texto[2:5])
    print(texto[:])

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
