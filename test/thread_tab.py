from threading import Thread
import time
from random import randint

class IlMioThread (Thread):
   def __init__(self, nome, durata):
      Thread.__init__(self)
      self.nome = nome
      self.durata = durata
   def run(self):
      print ("Thread '" + self.name + "' avviato")
      time.sleep(self.durata)
      print ("Thread '" + self.name + "' terminato")
      


thread1 = IlMioThread("Thread#1", randint(1,100))
thread1.start()
thread1.join()
