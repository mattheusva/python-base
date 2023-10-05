""" Calculadora Prefix

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
python prefix_calculadora.py sum 5 2
7
"""
__verion__ = "0.1.0"

import sys

arguments = sys.argv[1:]

if not arguments:
    operation = input("Insira a operação: ")
    n1 = input("Insira o número 1: ")
    n2 = input("Insira o número 2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Informe a operação, número1, número2")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")

if operation not in valid_operations:
    print("Informe uma operação válida")
    print(valid_operations)
    sys.exit(1)

valid_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    valid_nums.append(num)

n1, n2 = valid_nums

if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"O resultado é {result}")
