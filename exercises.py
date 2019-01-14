# coding: utf-8

## LIST OF EXERCISES !

"""
1) Escreva um algoritmo que contenha uma função de nome estudo() e que quando executada imprima na saída padrão a
frase "Estamos estudando as funções":
"""

#def estudo():
#    print("Estamos estudando as funções")

#estudo()


# RESPONDIDO :)

""" 
2) Escreva um código contendo uma função de nome estudo e defina que a mesma deva receber um número como argumento. 
Chame este argumento de x. No corpo da função imprima a seguinte frase na tela: "Função invocada com sucesso. 
O valor passado pelo argumento x é: <valor de x>"
"""

#def estudo(x):
#    print("Função invocada com sucesso. O valor passado pelo argumento x é:", x)

#estudo(10)

# RESPONDIDO :)

""" 
3) Escreva um algoritmo que receba dois números através da declaração de dois parâmetros cujos nomes serão: x e y. 
No bloco de instrução faça a soma de ambos valores e imprima o resultado no monitor:
"""

#def estudo(x, y):
#    soma = x + y
#    print(soma)

#estudo(10, 5)

# RESPONDIDO :)

"""
4) Escreva um algoritmo contendo uma função que necessite de três argumentos. Em seguida, imprima na tela os 
argumentos em ordem ascendente e, por fim, imprima a média aritmética:
"""
#def media(x, y, z):
#    print(x)
#    print(y)
#    print(z)

#    nota = (x + y + z) / 3
#    print(nota)
#media(10, 4, 8)

# RESPONDIDO :)

"""
5) Escreva uma função que contenha dois parâmetros. O primeiro deve ser obrigatório e o segundo facultativo:
"""

#def valores(nome, idade=20):
#    print(nome)
#    print(idade)

#valores("Victor")

# RESPONDIDO :)

"""
6) Escreva uma função que invocará outra função na qual tenha dois parâmetros definidos. Invoque a primeira função 
de ``func1()`` e a segunda de ``func2()``. Em seguida, invoque os parâmetros da segunda função de x e y. Some x e y e 
retorne o resultado. Em func1(), ao receber o resultado, retorne-o também como valor de retorno da função. Por fim, 
imprima na tela o valor que foi calculado por func2(), retornado para func1() e retornado a quem invocou a função 
inicialmente:
"""

#def func1():

#    def func2(x, y):
#        soma = x + y
#        return soma

#    return func2(50, 50)

#print(func1())

#func1()

# RESPONDIDO :)

"""
7) Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros. Em seguida, imprima os parâmetros recebidos na tela:
"""

# def n_parametros(*args):
#     print(args)

# n_parametros('bom dia', 'boa tarde', 'boa noite')

# RESPONDIDO :)

"""
8) Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros que estejam associados a uma chave. Em seguida, imprima na tela o nome da chave e o respectivo valor:
"""

# def n_parametros(**kwargs):
#     cadastro = {"nome": "Victor",
#                 "sobrenome":"Cruz",
#                 "idade": 20
#     }

    # print(cadastro)
    # print(kwargs)

# n_parametros(a=10, b=20, c=30, d=40, e=50)

# RESOLVIDO :)

"""
9) Considere o trecho de código a seguir.

    def func(a, b, c, d)
        print(a+b+c+d)
    lista = 1,2,3,4

Invoque a função func(), passando como argumento os valores contidos em lista, com a respectiva ordem, de forma a 
utilizar o conceito de desempacotamento:
"""

# def func(a, b, c, d):
#     print(a, b, c, d)

# lista = 1,2,3,4

# func(*lista)

# RESOLVIDO :)

"""
10) Escreva um algoritmo que encontre o maior dentre 3 números. Para facilitar a resolução do exercício utilize funções.
"""

#
# l_ = lista
# l_.sort()
#
# print(l_[len(l_)-1])
# print(l_[-1])


# def acha_maior(lista):
#     maior_numero = lista[0]
#
#     for x in lista:
#         if x > maior_numero:
#             maior_numero = x
#
#     return maior_numero
#
# print(acha_maior([5, 2, 10, 8]))
# print(acha_maior([50, 22, 101, 89]))
# print(acha_maior([55, 12, 0, 38]))


# numero_1 é 15
# intervalo é de 12 à 34






# def inter(intervalo, numero_1):
#     if numero_1 > intervalo[0] and numero_1 < intervalo[1]:
#         return True
#     else:
#         return False


# def inter(intervalo, numero_1):
#     return numero_1 > intervalo[0] and numero_1 < intervalo[1]
#
#
# # return True or False
#
#
# intervalo = (12, 34)
# numero_1 = 15
# numero_2 = 50
#
#
# print(inter(intervalo, numero_1))
# print(inter(intervalo, numero_2))


# def deduplica(input):
#     lista_ordenada = []
#     for i in items:
#         if i not in lista_ordenada:
#             lista_ordenada.append(i)



    # return lista_ordenada


# items = [1, 2, 3, 3, 3, 3, 4, 5]
# print(deduplica(items))
# [1, 2, 3, 4, 5]



# lista = "1234abcd"
#
# def inversao(inversao):
#
#     lista = inversao[::-1]
#     print(lista)
#
# inversao(lista)


lista = "1234abcd"

def inverter(lista):
    var = len(lista)
    print(var)

    nova_lista = ""
    while var >= 1:
        var -= 1
        nova_lista += lista[var]

    print(nova_lista)

inverter(lista)




















