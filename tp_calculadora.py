import functions


def menu():
    menu = """
        Menú:
        1. Ingresar 1er operando
        2. Ingresar 2do operando
        3. Operar 
        4. Informar resultados
        5. Salir
    """
    print(menu)

    selected_option = input("Escoge la opcion: ")
    return selected_option

def operations_options(a: float, b: float):
    while True:
        menu = f"""
            a. Calcular la suma ({a} + {b})
            b. Calcular la resta ({a} - {b})
            c. Calcular la division ({a} / {b})
            d. Calcular la multiplicacion ({a}*{b})
            e. Calcular factorial({a}!) y factorial({b}!)
        """
        print(menu)
        selected_option = input("Escoge la operacion: ")

        if selected_option in ('a', 'b', 'c', 'd', 'e'):
            return selected_option


def calculate_operation(a: float, b: float, operation: str):
    match operation:
        case "a":
            return f"El resultado de {a} + {b} es: {functions.suma(a, b)}"
        case "b":
            return f"El resultado de {a} - {b} es: {functions.resta(a, b)}"
        case "c":
            if b == 0:
                return "Err: no se puede dividir por 0"
            
            return f"El resultado de {a} / {b} es: {functions.division(a, b)}"
        case "d":
            return f"El resultado de {a} * {b} es {functions.multiplicacion(a, b)}"
        case "e":
            factorial_a, factorial_b = functions.factorial(a, b)
            return f"\nEl factorial de {a} es {factorial_a} \nEl factorial de {b} es {factorial_b}"


def get_operand(text: str):
    while True:
        try:
            value = float(input(text))
            return value
        except Exception:
            pass


def select_operations(a: float, b: float):
    if a is None:
        return print('no has elegido el primer operando')

    if b is None:
        return print('No has elegido el segundo operando')
    
    return operations_options(a, b)


def show_results(resultados: str):
    print(f'Los resultados obtenidos son los siguientes: {resultados}')


def calculator():
    first_number = None
    second_number = None
    operation = None
    results = None

    while True:
        match menu():
            case "1":
                first_number = get_operand('Ingrese el primer operando: ')
            case "2": 
                second_number = get_operand('Ingrese el segundo operando: ')
            case "3":
                operation = select_operations(first_number, second_number)
                results = calculate_operation(a=first_number, b=second_number, operation=operation)
            case "4":
                if operation is None:
                    print('No has elegido una operacion a realizar')
                    continue

                show_results(results)
            case "5":
                print("Saliste de la calculadora")
                break
            case _:
                print("Opcion invalida")

calculator()