def slice_advanced():
# Código a implementar utilizando input.
  # Defino el primer texto:
 txt2 = "Hello, World!"

 # Printeo sus diviciones:

 #  0   1   2   3   4   5   6   7   8   9   10  11  12
 # (H   e   l   l   o   ,   -   W   o   r   l   d   !)
 # -13 -12 -11 -10  -9 -8  -7  -6  -5  -4  -3  -2  -1

 # Primer texto:
 print(txt2[4::2])

 # Defino el segundo texto:
 txt3 = "12345678910"

 # Printeo sus particiones:

 #  0   1   2   3   4   5   6   7   8   9     
 # (1   2   3   4   5   6   7   8   9  10)
 # -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

 # Segundo texto:
 print(txt3[4::2])

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`
