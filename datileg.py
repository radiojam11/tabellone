import pickle
infile = open('1dati.bin','rb')
dati = pickle.load(infile)
infile.close()
print(dati)

for el in dati:
    if int.from_bytes(el, 'big'):
        print("trovato un address valido")
        