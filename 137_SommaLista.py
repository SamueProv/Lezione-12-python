N = int(input("Inserisci N: "))
numeri = [random.randint(1, 20) for _ in range(N)]
print(numeri)
print("Somma:", sum(numeri))