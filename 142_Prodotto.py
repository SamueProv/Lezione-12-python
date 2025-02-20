numeri = [random.randint(1, 10) for _ in range(10)]
prodotto = 1
for n in numeri:
    prodotto *= n
print(numeri)
print("Prodotto:", prodotto)