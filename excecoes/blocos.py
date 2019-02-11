# coding: utf-8

### Código sem tanta lógica

b = 2
def erro(x):
    try:
        eval(x)
    except (TypeError, NameError):
        print("Ocorreu aqui um TypeError ou então um NameError")
    except ValueError:
        print("Não pode transfomar B em um número inteiro")
    except ZeroDivisionError:
        print("Impossível dividir um número por zero")
    else:
        print("Nenhuma exceção ocorreu.")
        print(x)




# TypeError
# erro("int+int") # Função 'int' converte do tipo string para o tipo inteiro

# NameError
# erro("a")

# ValueError
# erro("int('b')")

# ZeroDivisionError
# erro("2/0")

erro()

