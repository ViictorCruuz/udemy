#coding: utf-8

# EXEMPLO DE DESEMPACOTAMENTO

lista = [11, 10, 12]
tupla = (11, 10, 12)


def func(a, b, c):
    print(a)
    print(b)
    print(c)

l = [*tupla]
# l = list(tupla)
l.sort()
func(*l)