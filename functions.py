def suma(a, b):
    """Esta funcion recibe dos valores numericos y retorna la sumatoria de ambos"""
    return a + b

def resta(a, b):
    """Esta funcion recibe dos valores numericos y retorna la resta de ambos"""
    return a - b

def division(a, b):
    """Esta funcion recibe dos valores numericos y retorna la division de ambos"""
    return a / b

def multiplicacion(a, b):
    """Esta funcion recibe dos valores numericos y retorna la multiplicacion de ambos"""
    return a * b

def factorial(a, b):
    """Esta funcion recibe dos valores numericos y retorna el factorial de ambos"""

    def do_factorial(value: int) -> int:
        contador = 1

        while value > 1:
            contador = contador * value
            value -= 1

        return contador
    
    return do_factorial(a), do_factorial(b)
