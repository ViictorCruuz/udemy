# precisaremos usar isso logo adiante ...
from functools import partial

# a função que facilita a criação de nossas "classes"
def newClass(nome, atributos):
    cls = {}
    for k, v in atributos.items():
        cls[k] = v
    return cls

### Classe Pessoa

# construtor, correspondente ao __new__ de Python
def newPessoa(nome, nascimento):
    inst = {} # a nova instância
    inst['classe'] = Pessoa # a instância tem de saber a que classe pertence

    # Agora a instância vai criar os métodos embrulhando as chamadas
    # para as funções originais em uma nova, já se incluindo nela
    for k, v in Pessoa.items():
        #se for função...
        if callable(v):
            # é, então vamos embrulhar...
            metodo = partial(v, inst)
            # a linha acima equivale a: lambda *a, **k(inst, *a, **k)
            # mas não podemos usar isso pois as variáveis nos loops
            # são passadas simbolicamente e acabaríamos somente com a
            # última chamada.
            inst[k] = metodo
    inst['nome'] = nome
    inst['nascimento'] = nascimento
    return inst

def idade(inst, hoje):
    hd, hm, ha = hoje
    nd, nm, na = inst['nascimento']
    x = ha - na
    return x

Pessoa = newClass('Pessoa', {'newPessoa':newPessoa, 'idade':idade})
### Fim da definição de classe

hank = Pessoa['newPessoa']('Victor Cruz', (28, 12, 1998))

# Como agora temos o metodo idade no dicionário instância e ele sabe a
# quem pertence, podemos fazer a chamada direto

print(hank['idade']((4, 2, 2019)))

# Para garantir que está funcionando mesmo, vamos criar uma nova
# instância com valores diferentes

"""
    Aqui eu posso criar
    uma nova instância
    com qualquer valor
    que eu quiser, tanto
    nome quanto idade
"""

