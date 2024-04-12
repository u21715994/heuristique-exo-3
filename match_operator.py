from operation_functionality import add, subtract, multiply, divide

def match_operator(operator):
    match operator:
        case '+':
            calculate_function = add
            operator_function = "(addition)"
        case '-':
            calculate_function = subtract
            operator_function = "(soustraction)"
        case '*':
            calculate_function = multiply
            operator_function = "(multiplication)"
        case '/':
            calculate_function = divide
            operator_function = "(division)"
        case _:
            print('Invalid operator')
    return calculate_function, operator_function