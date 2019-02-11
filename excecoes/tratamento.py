# coding: utf-8

logger = "mensagem de erro"

def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print("ValueError")
        print(type(e)) #instância da exceção ( De qual classe essa exceção foi criada )
        print(e.args) #argumentos das mensagens
        print(e) # o valor da varável __str__  (valor interno onde definimos uma mensagem) 

# ValueError
erro("int('b')")