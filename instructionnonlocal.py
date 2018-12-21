# coding: utf-8

# INSTRUÇÃO NONLOCAL

def func():
    print("Welcome")

    var_local = 10

    def func_interna():
        nonlocal var_local
        var_local += 1
        print(var_local)

    func_interna()

func()


x = 20
def funcX():
    global x
    return x

print(funcX())