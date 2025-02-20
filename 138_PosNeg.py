N = int(input("Inserisci N: "))
numeri = [random.randint(-20, 20) for _ in range(N)]
pos = sum(n for n in numeri if n > 0)
neg = sum(n for n in numeri if n < 0)
print(numeri)
print("Somma positivi:", pos, "Somma negativi:", neg)