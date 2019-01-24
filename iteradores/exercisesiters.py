xl = list(range(1, 100, 1))

for n in xl:
    print(n)

a = int(input("Escreva o número inicial do intervalo: "))
b = int(input("Escreva o número final do intervalo: "))

while (a == b) == True:
    print("Escreva números diferentes")
    break

for i in range(a, b, 1):
    print(i)


print("=====================================")
print("=====================================")
print("=====================================")

for n in range(10, 0, -1):
    print(n)

print("=====================================")
print("=====================================")
print("=====================================")


for p in range(0, 100, 2):
    print(p)

print("=====================================")
print("=====================================")
print("=====================================")

soma = 0

for n in range(1, 100):

    if n < 100:
        if n %2 == 0:
            soma += 1
            continue
else:
    print(soma)

print("=====================================")
print("=====================================")
print("=====================================")


primos = []

for numero in range(1, 100):
    contador = 0

    for numeroPrimo in range(1, numero+1):
        if numero % numeroPrimo == 0:
            contador += 1

    if contador <= 2:
        primos.append(numero)
print(primos)


print("=====================================")
print("=====================================")
print("=====================================")















