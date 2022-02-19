from itertools import permutations
import tkinter as tk
from tkinter import ttk
from datetime import datetime

team_left = "Grosseto A.S."
team_right = "Roccacannuccia"
periodo = 3
team_scoreL = 39
team_scoreR = 119
tempo = datetime.now().strftime('%H:%M:%S')
falliL = 3
falliR = 5

carattere = "Helvetica"
colore_team = "#06B5C3"
colore_punti = "#E85811"
colore_tempo = "#31A745"


def aggiorna():
    tempo = datetime.now().strftime('%H:%M:%S')
    timerpartita.config(text=tempo)
    root.after(200, aggiorna)

# root window
root = tk.Tk()
root.geometry("1200x800")
root.title('Tabellone')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=4)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=4)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=2)
root.rowconfigure(2, weight=2)
root.rowconfigure(3, weight=2)

# TEAM LEFT
team_nameL_label = ttk.Label(root, text=team_left, font=(carattere, 40), foreground=colore_team)
team_nameL_label.grid(column=0, row=0,  padx=5, pady=5)
# sticky=tk.EW,

# TEAM RIGHT
team_nameR_label = ttk.Label(root, text=team_right, font=(carattere, 40), foreground=colore_team)
team_nameR_label.grid(column=2, row=0,  padx=5, pady=5)

# TEAM SCORE LEFT
team_scoreL_label = ttk.Label(root, text=team_scoreL, font=(carattere, 130), foreground=colore_punti)
team_scoreL_label.grid(column=0, row=1,  padx=5, pady=5)

# TEAM SCORE RIGHT
team_scoreR_label = ttk.Label(root, text=team_scoreR, font=(carattere, 130), foreground=colore_punti)
team_scoreR_label.grid(column=2, row=1,  padx=5, pady=5)

# Periodo
periodo_label = ttk.Label(root, text=periodo, font=(carattere, 50), foreground=colore_tempo)
periodo_label.grid(column=1, row=1 ,  padx=5, pady=5)

# Timer
timerpartita = ttk.Label(root, text=tempo, font=(carattere, 130), foreground=colore_tempo)
timerpartita.grid(column=0, columnspan=3 , row=2 ,  padx=5, pady=5)

# FAULS LEFT
faulsL_label = ttk.Label(root, text=falliL, font=(carattere, 130), foreground=colore_punti)
faulsL_label.grid(column=0, row=3,  padx=5, pady=5)
# sticky=tk.EW,

# FAULS RIGHT
faulsR_label = ttk.Label(root, text=falliR, font=(carattere, 130), foreground=colore_punti)
faulsR_label.grid(column=2, row=3,  padx=5, pady=5)

aggiorna()
root.mainloop()

