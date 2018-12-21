# coding: utf-8

# FUNÇÕES ANINHADAS

# from variadic import argumentos
#
#
# def func():
#     print("func")
#
#     def func_interna():
#         print("func_interna")
#
#     func_interna()
#
#     argumentos("Olá")
#
#
# if __name__ == '__main__':
#     func()


def func():
    print("func")

    def internal_func():
        print("internal_func")

    internal_func()

func()


