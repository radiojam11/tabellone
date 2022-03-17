# TecnoGeppetto 2022 sistema di lettura dati da Tabellone Sportivo
# i dati sono ricostruiti in un tabellone "digitale" su GUI
#

# GUI e visualizzazione

from re import A
import tkinter as tk
from tkinter import ttk
import serial , funzioni
import os
#from time import time
import pickle

# INDIRIZZI DEL MESSAGGIO INTERCETTATO
address_rid = {
    b"\x80":("game_clock", 12),
    b"\x82":("team_scores", 12),
    b"\x83":("team_fouls", 12),
    b"\x92":("team_name_left", 14),
    b"\x93":("team_name_right", 14)
}

# VARIABILI  (da prelevare da flusso dati)
addr_diz={
   "team_left" : "Squadra a.",
   "team_right" : "Squadra b.",
   "periodo" : "1",
   "team_scoreL" : "001",
   "team_scoreR" : "000",
   "tempo" : "22:22",
   "falliL" : " 0",
   "falliR" : " 0"
}

# FONT
carattere = "Digital-7"
#carattere = "Helvetica"

# COLORI
colore_team = "#06B5C3"
colore_punti = "#E85811"
colore_tempo = "#31A745"


# ************************************  GUI *********************************

def benvenuto():
    team_nameL_label.config(text="Benvenuto")
    team_nameR_label.config(text="TecnoGeppetto")
    periodo_label.config(text="by")
    
def regard():
    team_nameL_label.config(text="Copia")
    team_nameR_label.config(text="Registrata")
    periodo_label.config(text="ok")
    
def aggiornaGUI():
      #star = time()
                   
      # aggiorno i dati sulla GUI
      team_nameL_label.config(text=addr_diz["team_left"])
      team_nameR_label.config(text=addr_diz["team_right"])
      team_scoreL_label.config(text=addr_diz["team_scoreL"])
      team_scoreR_label.config(text=addr_diz["team_scoreR"])
      periodo_label.config(text=addr_diz["periodo"])
      timerpartita.config(text=addr_diz["tempo"])
      faulsL_label.config(text=addr_diz["falliL"])
      faulsR_label.config(text=addr_diz["falliR"])
      
      # leggo i dati da RS485 e scrivo il dizionario che aggiorna il tabellone
      ser.flush()       # pulisco la coda sella seriale
      mes = ser.read()  # leggo il primo byte nella coda della seriale
      
      if mes in address_rid.keys():    # se è un indirizzo valido prendo il numero di bytes pari alla lunghezza del messaggio 
             #                         # che conosco e lo faccio processare da funzioni.handle_funz
             nome, packet_length = address_rid[mes]
             #print(nome)
             messaggio = ser.read(packet_length-1) # l'indirizzo che fa parte della lunghezza del messaggio l'ho già preso
             messaggio = messaggio[:-1]            # per il momento tolgo anche il CRC in fondo al messaggio  * per ora non faccio il controllo dell'errore
             print(messaggio)
             x =(funzioni.handle_funz(nome , messaggio)) # lavoro il messaggio con il file funzioni per ottenere un dizionario con le Key aggiornate
             # aggiorno il dizionario addr_diz da cui legge la GUI
             for key in x.keys():
                    addr_diz[key] = x[key]
      
      
      #end = time()
      #if (end - star)>0.1:
      #print("Time---: ", end - star)

      root.after(1, aggiornaGUI)

# root window
root = tk.Tk()
root.geometry("1100x800")
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
timerpartita = ttk.Label(root, text="", font=(carattere, 240),background='black', foreground=colore_tempo)
timerpartita.grid(column=0, columnspan=3 , row=2 ,  padx=5, pady=5)

# FAULS LEFT
faulsL_label = ttk.Label(root, text="", font=(carattere, 120),background='black', foreground=colore_punti)
faulsL_label.grid(column=0, row=3,  padx=5, pady=5)
# sticky=tk.EW,

# FAULS RIGHT
faulsR_label = ttk.Label(root, text="", font=(carattere, 120),background='black', foreground=colore_punti)
faulsR_label.grid(column=2, row=3,  padx=5, pady=5)

# ******************************************  GUI END *********************************
benvenuto()
funzioni.controlla_copia()

# STAMPO LA LISTA DELLE SERIALI A VIDEO e  CHIEDO IMMISSIONE DEL NOME DELLA PORTA CORRETTA con funzioni.ser_dispo()
ser = serial.Serial(funzioni.ser_dispo(), baudrate=19200, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_ODD  , timeout=15)
ser.flush()
aggiornaGUI()
root.mainloop()

