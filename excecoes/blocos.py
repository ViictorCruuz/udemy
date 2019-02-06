# coding: utf-8

### Código sem tanta lógica


def erro(x):
    try:
        eval(x)
    except TypeError:
        print("Você não pode somar a função duas funções do mesmo tipo")
    except NameError:
        print("A sua variável não foi definida")
    except ValueError:
        print("Não pode transfomar B em um número inteiro")
    except ZeroDivisionError:
        print("Impossível dividir um número por zero")

# TypeError
erro("int+int") # Função 'int' converte do tipo string para o tipo inteiro

# NameError
erro("a")

# ValueError
erro("int('b')")

# ZeroDivisionError
erro("2/0")

