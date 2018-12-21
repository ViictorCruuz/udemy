# coding: utf-8

# FUNÇÕES VARIÁDICAS

# def lista_de_argumentos(*lista):
#     lista = [10,20,30,40,50]
#     list = ["um", "dois", "três", "quatro"]
#     return lista, list
#
# print(lista_de_argumentos())

def lista_de_argumentos(*args):
    print(args)

def lista_de_argumentos_associativos(**kwargs):
    print(kwargs)

def argumentos(*args, *kwargs):
    print(args)
    print(kwargs)

# argumentos(1,2,3,4,5, um=1, dois=2, tres=3, quatro=4, cinco=5)


# lista_de_argumentos(1,2,3,4,5,6)
# lista_de_argumentos("um", "dois", "três", "quatro")
#
# lista_de_argumentos_associativos(a=1, b=2, c=3, d=4)
# lista_de_argumentos_associativos(um=1, dois=2, tres=3, quatro=4)

if __name__ == '__main__':
    argumentos(1, 2, 3, 4, 5, um=1, dois=2, tres=3, quatro=4, cinco=5)
