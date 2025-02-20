N = int(input("Inserisci N: "))
numeri = [random.randint(1, 100) for _ in range(N)]
pari = sum(1 for n in numeri if n % 2 == 0)
dispari = N - pari
print(numeri)
print("Pari:", pari, "Dispari:", dispari)