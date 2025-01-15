# Función que suma dos números
def sum(a, b):
    # Se utiliza doctest para realizar pruebas dinámicas en esta función.
    # A continuación se muestra cómo usar doctest para validar que la suma de dos números
    # se realiza correctamente.
    #
    # Para ejecutar las pruebas, puedes utilizar el siguiente comando en tu terminal:
    # python -m doctest src/calculator.py
    
    # Ejemplo de prueba con doctest: 
    # >>> sum(5, 7)
    # 12
    # >>> sum(4, -4)
    # 0
    """
    >>> sum(5,7)
    12
    
    >>> sum(4, -4)
    0
    """
    # Retorna la suma de los dos valores pasados como parámetros
    return a + b

# Función que resta dos números
def subtract(a, b):
    # La función devuelve la diferencia entre 'a' y 'b'
    return a - b

# Función que multiplica dos números
def multiplication(a, b):
    # La función devuelve el resultado de la multiplicación de 'a' por 'b'
    return a * b

# Función que realiza una división entre dos números
def division(a, b):
    # Esta función contiene pruebas dinámicas que se pueden ejecutar con doctest para verificar
    # que la división maneja correctamente los casos, especialmente cuando se intenta dividir por 0.
    #
    # Ejemplo de prueba con doctest:
    # >>> division(10, 0)
    # Traceback (most recent call last):
    # ValueError("La división por 0 no está permitida")
    
    """
    >>> division(10,0)
    Traceback (most recent call last):
    ValueError("La división por 0 no está permitida")
    """
    # Si 'b' es 0, se lanza un error indicando que no es posible dividir por 0.
    if b == 0:
        raise ValueError("La división por 0 no está permitida")
    
    # Retorna el resultado de la división si 'b' no es 0
    return a / b