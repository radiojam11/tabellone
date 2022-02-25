import pickle
infile = open('4dato.bin','rb')
dati = pickle.load(infile)
infile.close()
print(dati)

for el in dati:
    print(int.from_bytes(el, 'big'))
        