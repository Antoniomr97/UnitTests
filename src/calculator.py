def sum(a, b):
    # Pruebas dinamicas con python -m doctest src/calculator.py, utilizando doctest
    """
    >>> sum(5,7)
    12
    
    >>> sum(4, -4)
    0

    """
    return a + b

def subtract(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):

    """
    
    >>> division(10,0)
    Traceback (most recent call last):
    ValueError("La división por 0 no está permitida")
    """

    if b == 0:
        raise ValueError("La división por 0 no está permitida")
    return a / b