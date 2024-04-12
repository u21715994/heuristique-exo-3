def print_calcul(total, calculate_function, numbers, operator, operator_function):
    print(total)
    for i in range(len(numbers)-1):
        total = calculate_function(total, numbers[i+1])
        print(operator + str(numbers[i+1]))
    print("-------")
    print("total = " + str(total) + " " + operator_function)