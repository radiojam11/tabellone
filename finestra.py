# TecnoGeppetto 2022 sistema di lettura dati da Tabellone Sportivo
# i dati sono ricostruiti in un tabellone "digitale" su GUI
#
# GUI e visualizzazione

import tkinter as tk
from tkinter import ttk
# qui sotto solo per DEMO finche' non si aggancia al flusso dati
from datetime import datetime
from random import *
from threading import Thread

minuti = datetime.now().strftime('%M:%S')
#VARIABILI  (da prelevare da flusso dati)
addr_diz={
"team_left" : "Grosseto A.S.",
"team_right" : "Roccacannuccia",
"periodo" : 3,
"team_scoreL" : 139,
"team_scoreR" : 119,
"tempo" : minuti,
"falliL" : 3,
"falliR" : 5
}

# FONT
carattere = "Digital-7"
#carattere = "Helvetica"

#COLORI
colore_team = "#06B5C3"
colore_punti = "#E85811"
colore_tempo = "#31A745"


def aggiorna():
    # AGGANCIARE QUI LE VARIABILI AL FLUSSO DEI DATI
    team_nameL_label.config(text=addr_diz["team_left"])
    team_nameR_label.config(text=addr_diz["team_right"])
    team_scoreL_label.config(text=addr_diz["team_scoreL"])
    team_scoreR_label.config(text=addr_diz["team_scoreR"])
    periodo_label.config(text=addr_diz["periodo"])
    timerpartita.config(text=addr_diz["tempo"])
    faulsL_label.config(text=addr_diz["falliL"])
    faulsR_label.config(text=addr_diz["falliR"])
    
    root.after(1000, aggiorna)

# root window
root = tk.Tk()
root.geometry("1200x800")
root.title('Tabellone by TecnoGeppetto')
root.resizable(0, 0)
root['bg'] = 'black'

# configure the grid
root.columnconfigure(0, weight=4)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=4)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=2)
root.rowconfigure(2, weight=2)
root.rowconfigure(3, weight=2)

# TEAM LEFT
team_nameL_label = ttk.Label(root, text="", font=(carattere, 60),background='black', foreground=colore_team)
team_nameL_label.grid(column=0, row=0,  padx=5, pady=5)
# sticky=tk.EW,

# TEAM RIGHT
team_nameR_label = ttk.Label(root, text="", font=(carattere, 60),background='black', foreground=colore_team)
team_nameR_label.grid(column=2, row=0,  padx=5, pady=5)

# TEAM SCORE LEFT
team_scoreL_label = ttk.Label(root, text="", font=(carattere, 180),background='black', foreground=colore_punti)
team_scoreL_label.grid(column=0, row=1,  padx=5, pady=5)

# TEAM SCORE RIGHT
team_scoreR_label = ttk.Label(root, text="", font=(carattere, 180),background='black', foreground=colore_punti)
team_scoreR_label.grid(column=2, row=1,  padx=5, pady=5)

# Periodo
periodo_label = ttk.Label(root, text="", font=(carattere, 90),background='black', foreground=colore_tempo)
periodo_label.grid(column=1, row=1 ,  padx=5, pady=5)

# Timer
timerpartita = ttk.Label(root, text="", font=(carattere, 180),background='black', foreground=colore_tempo)
timerpartita.grid(column=0, columnspan=3 , row=2 ,  padx=5, pady=5)

# FAULS LEFT
faulsL_label = ttk.Label(root, text="", font=(carattere, 180),background='black', foreground=colore_punti)
faulsL_label.grid(column=0, row=3,  padx=5, pady=5)
# sticky=tk.EW,

# FAULS RIGHT
faulsR_label = ttk.Label(root, text="", font=(carattere, 180),background='black', foreground=colore_punti)
faulsR_label.grid(column=2, row=3,  padx=5, pady=5)


class XThread (Thread):
   def __init__(self, nome):
      Thread.__init__(self)
      self.name = nome
   def run(self):
      print ("Thread '" + self.name + "' avviato")

      


thread1 = XThread("Gestione Dati da RS485")
thread1.start()
thread1.join()
aggiorna()
root.mainloop()


