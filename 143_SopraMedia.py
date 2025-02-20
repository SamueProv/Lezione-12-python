numeri = [random.randint(1, 10) for _ in range(10)]
media = sum(numeri) / len(numeri)
sopra_media = sum(1 for n in numeri if n > media)
print(numeri)
print("Sopra media:", sopra_media)