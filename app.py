import sys
from output import print_calcul
from match_operator import match_operator
from input_read import input_read

csv_file_name = sys.argv[1]
operator = sys.argv[2]
operator_function = ""


numbers = input_read(csv_file_name)
numbers = list(map(int, numbers))
calculate_function, operator_function = match_operator(operator)

total = numbers[0]

print_calcul(total, calculate_function, numbers, operator, operator_function)