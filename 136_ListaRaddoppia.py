numeri = [random.randint(1, 100) for _ in range(10)]
numeri = [n*2 if n % 2 != 0 else n for n in numeri]
print(numeri)
