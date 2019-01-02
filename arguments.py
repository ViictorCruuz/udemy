# coding: utf-8

## ARGUMENTOS POSICIONAIS E ARGUMENTOS NOMEADOS

#def dados_pessoais(nome, sobrenome, idade, sexo):
#    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
#            .format(nome, sobrenome, idade, sexo))

#dados_pessoais("Victor", "Cruz", 18, True)  # > Passados argumentos de forma posicional
#   dados_pessoais(sobrenome="Cruz",
#                 sexo=True,
#                 nome="Victor",
#                 idade=19) # > Passados argumentos de forma nomeado

def ficha_de_cadastro(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
            .format(nome, sobrenome, idade, sexo))

ficha_de_cadastro(sobrenome="Cruz",
                  sexo=True,
                  nome="Victor",
                  idade=20)