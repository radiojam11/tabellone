# TecnoGeppetto 2022
# sistema per certificare l'uso di un programma 
# questo file serve per legare la una macchina all'uso di un certo programma.
# non fa altro che leggere il seriale dell'HD, registrare quindi il file config.bin che conterra' le info della macchina autorizzata
# all'uso del programma, poi si auto-cancella
# naturalmente il programma cosi protetto deve contenere la stessa routine che vada a leggere il config.bin 
# e controllare che la macchina su cui si sta utilizzando il programma sia effettivamente quella autorizzata 
# #

import pickle , os
from time import sleep
import sys, subprocess 

f = os.popen('vol')
s = f.read()
s=s[s.index(":")+1:-1]
print(s)
pickle.dump( s, open( "config.bin", "wb" ) )
sleep(1)
subprocess.Popen("python -c \"import os, time; time.sleep(1); os.remove('registra.exe');\"")   # va modificato col nome del file definito
sys.exit(0)
# copiare questo file e chiamarlo registra.py per ottenere l'eseguibile con il nome corretto    
#  pyinstaller --onefile nome_file.py                              # per farlo partire e compilarlo in EXE