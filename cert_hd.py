import pickle , os
from time import sleep

f = os.popen('vol')
s = f.read()
s=s[s.index(":")+1:-1]
print(s)
pickle.dump( s, open( "config.bin", "wb" ) )
sleep(1)
try:
    os.popen('del registra.exe')
except:
    raise NameError('Buon Lavoro')
# copiare questo file e chiamarlo registra.py per ottenere l'eseguibile con il nome corretto    