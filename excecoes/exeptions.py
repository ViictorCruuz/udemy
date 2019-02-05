# try:
#     a = 10 / 0
#     print(a)
# except ZeroDivisionError:
#     print("Não é possível dividir um número por zero.")
#

#
# def input_float(msg):
#     while True:
#         try:
#             return float(input(msg))
#         except ValueError:
#             print("Número inválido.")
#
#
# num1 = input_float("Digite o primeiro número: ")
# num2 = input_float("Digite o segundo número: ")
#
# try:
#     print(num1 / num2)
# except ZeroDivisionError:
#     print("Não é possível dividir um número por zero.")


def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Isso não é número, tente novamente!!!")

number1 = input_int(("Write the first number: "))
number2 = input_int(("Write the second number: "))

print(number1 * number2)