# # precisaremos usar isso logo adiante ...
# from functools import partial

# # a função que facilita a criação de nossas "classes"
# def newClass(nome, atributos):
#     cls = {'nome':nome}
#     for k, v in atributos.items():
#         if k == 'new'+nome:
#             v = partial(v, cls)
#     # e atribuímos tudo normalmente
#     cls[k] = v
#     return cls

# ### Classe Pessoa
# # construtor, corresponde ao __new__ de Python
# def newPessoa(cls, nome, nascimento): # agora a classe mesmo vem aqui
#     inst = {} # a nova instância
#     inst['classe'] = Pessoa # a instância tem de saber a que classe pertence

#     for k, v in Pessoa.items():
#         # Se for função...
#         if callable(v):
#             # é, então vamos embrulhar...
#             metodo = partial(v, inst)
#             inst[k] = metodo

#     # a própria newPessoa vai chamar initPessoa()
#     inst['inst'+cls['nome']](nome, nascimento)
#     return inst

# # inicializador, corresponde ao __init__ de Python
# def __init__(self, nome, nascimento):
#     self.nome = nome
#     self.nascimento = nascimento
#     # assim como fazemos normalmente no __init__, aqui não precisamos
#     # nos preocupar

# def idade(self, hoje):
#     hd, hm, ha = hoje
#     nd, nm, na = self.nascimento
#     x = ha - na
#     return x

# # e agora initPessoa() tem de entrar aqui também
# Pessoa = newClass('Pessoa', {'newPessoa':newPessoa,
#                              'initPessoa':initPessoa,
#                              'idade':idade})
# ### Fim da definição de classe

# hank = Pessoa('Victor Cruz', (28, 12, 1998))

# # Como agora temos o metodo idade no dicionário instância e ele sabe a
# # quem pertence, podemos fazer a chamada direto

# print(hank['idade']((4, 2, 2019)))

# # Para garantir que está funcionando mesmo, vamos criar uma nova
# # instância com valores diferentes

# fante = Pessoa['newPessoa']('Fanta', (5,5,1809))
# print(fante['idade']((4, 2, 2019)))

# """
#     Aqui eu posso criar
#     uma nova instância
#     com qualquer valor
#     que eu quiser, tanto
#     nome quanto idade
# """

