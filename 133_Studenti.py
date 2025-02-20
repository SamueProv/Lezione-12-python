studenti = []
studenti_classe = ["Nome1", "Nome2", "Nome3", "Nome4", "Nome5"]
for _ in range(5):
    nome = input("Inserisci un nome: ")
    if nome in studenti_classe and nome not in studenti:
        studenti.append(nome)
    else:
        print("Questo studente non va inserito nella classe")