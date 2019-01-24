# x, y = int(input("Início: ")), int(input("Fim: "))

# a, b, c = int(input("Ignorável 1: ")), int(input("Ignorável 2: ")), int(input("Ignorável 3: "))

# for n in range(x, y + 1, 1):
#     if (n==a or n==b or n==c):
#         continue
#     print(n)


print(" ===== VOCÊ ENTROU NO LOOP ===== ")
print()
for n in range(0, 500):
    print("STATUS: Ainda estou em looping")
    print()
    sair = input("Aperte uma tecla para sair do looping: ")
    print()
    if sair == "q":
        break
    else:
        continue
print(" ===== VOCÊ SAIU DO LOOP ===== ")
