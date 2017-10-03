test = {'Høyre': 'H', 'Venstre':'V', 'Rødt':'R'}

print(test['Venstre'])

blokk = {'H':'Borgerlig', 'V': 'Borgerlig', 'R': 'Sosialistisk'}

for parti, bokstav in test.items():
    print(f"{parti} har bokstaven {bokstav}, og er et {blokk[bokstav]} parti." )

print(list(test))
print(list(test.values()))