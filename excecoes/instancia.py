# ### Classe Pessoa

# Pessoa = {}
# # construtor, corresponde ao __new__ de Python
# def newPessoa(nome, nascimento):
#     new = {}
#     new['nome'] = nome
#     new['nascimento'] = nascimento
#     return new

# Pessoa['new'] = newPessoa
# ### Fim da definicao de classe

# # Ou seja, agora se queremos criar uma nova instancia, fazemos:
# hank = Pessoa['new']('Victor Cruz', (28, 12, 1998))

# # Tudo como esperado, temos os dados no dicionario
# hank['nome']
# hank['nascimento']


### Uma função que facilita a criação de nossas "classes"

def newClass(nome, atributos):
    cls = {} # cria um dicionário vazio para a classe
    for k, v in atributos.items(): # atribui os atributos (métodos e atributos de classe)
        cls[k] = v
    return cls

### Classe Pessoa, agora usando a função

# construtor, corresponde ao __new__ de Python
def newPessoa(nome, nascimento):
    inst = {} # a nova instância
    inst['classe'] = Pessoa
    inst['nome'] = nome
    inst['nascimento'] = nascimento
    return inst

def idade(inst, hoje):
    hd, hm, ha = hoje
    nd, nm, na = inst['nascimento']
    idade = ha - na
    return idade

# agora o método idade tem de entrar aqui também
Pessoa = newClass('Pessoa', {'newPessoa':newPessoa, 'idade':idade})
### Fim da definição de classe

# E a classe Pessoa continua funcionando da mesma maneira na hora de criar uma instância
hank = Pessoa['newPessoa']('Victor Cruz', (28, 12, 1998))

# Claro que aqui posso usar apenas a função idade() diretamente, mas intenção
# ao programar 00 não é essa.

""" idade(hank, (4, 2, 2019)) """

# Lembre que o método pertence à classe, não a instância. Não existe a chave 'idade'
# no dicionário da instância, tenho de usar o dicionário que corresponde à classe.

hank['classe']['idade'](hank, (4, 2, 2019))

