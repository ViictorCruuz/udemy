tel = {
    30301122: "Pericles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tieste"
}

print(tel)

print(len(tel))
print(tel.keys()) # Pode ser substituído por tel.get(<chave>)
print(tel.get(30301122))

print(tel.values()) # 
# print(del(tel["chave"]))
del(tel[36458899])
print(tel)
print(tel.popitem()) # Essa função retorna um elemento e ao mesmo tempo a remove
print(tel)

tel2 = {
    55551111: "Victor",
    99998888: "João"
}
print(tel2)

tel.update(tel2)
print(tel)