import pickle , serial
infile = open('4dato.bin','rb')
dati = pickle.load(infile)
infile.close()
#print(dati)

with serial.Serial('COM5', baudrate=19200, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_ODD  , timeout=15) as ser:
    while True:
        for el in dati:
            #print(int.from_bytes(el, 'big'))
            #print(el)
            ser.write(el)
        print('fine ciclo')
            