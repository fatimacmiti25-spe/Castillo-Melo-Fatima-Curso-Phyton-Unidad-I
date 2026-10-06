# 1. BUCLE FOR

frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)


# 2. BUCLE WHILE

contador = 0

while contador < 5:
    print(contador)
    contador += 1


# 3. BREAK

contador = 0

while True:
    print(contador)
    contador += 1

    if contador == 5:
        break


# 4. CONTINUE

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


# 5. PASS

for i in range(5):
    pass