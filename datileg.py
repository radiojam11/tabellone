import pickle
infile = open('1dati.bin,'rb')
dati = pickle.load(infile)
infile.close()
print(dati)
