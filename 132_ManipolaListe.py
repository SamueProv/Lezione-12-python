studenti.append("TuoNome")
studenti.append("NomeVicino")
studenti.insert(3, "CompagnoClasse")
del studenti[1]
studenti.remove("Teresa")
for i, nome in enumerate(studenti):
    print(i, nome)