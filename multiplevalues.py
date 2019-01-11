# coding: utf-8

# RETORNO DE VALORES

# def func():
#     return 1, 2
#
# a,b = func()
#
# print(a)
# print(b)

def potencia(x):
    quadrado = x**2
    cubo = x**3

    return quadrado, cubo

q, c = potencia(10)

print(q)
print(c)
