# coding: utf-8

# INSTRUÇÃO NONLOCAL

def new():
    print("Hello World !!!")

    var_lol = 20

    def function_interna():
        nonlocal var_lol
        var_lol += 5
        print(var_lol)

    function_interna()

new()




def func():
    print("Welcome")

    var_local = 10

    def func_interna():
        nonlocal var_local
        var_local += 1
        print(var_local)

    func_interna()

func()


var = 30
def funcao():
    global var
    return var
print(funcao())



