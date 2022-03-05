# TecnoGeppetto 2022
# Contiene le funzioni  che fanno il parsing e compongono il messaggio
# 
from ast import Try


def handle_funz(address, messaggio_byte):
    """ Seleziona la giusta funzione in base all'indirizzo del messaggio"""
    if address == "game_clock":
        return game_clock(address, messaggio_byte)
    elif address == "team_scores":
        return team_scores(address, messaggio_byte)
    elif address == "team_fouls":
        return team_fouls(address, messaggio_byte)
    elif address == "team_name_left":
        return team_name_left(address, messaggio_byte)
    elif address == "team_name_right":
        return team_name_right(address, messaggio_byte)
    else:
        return
    
def game_clock(address, messaggio_byte):
    # [0x80] = 128 Game clock + Possession + Timeout
    #if messaggio_byte[0] == b'G' :
        # Chronometer is counting, game time    Address 0x80
    messaggio_byte = messaggio_byte.decode()
    tempo = "{}{}{}{}{}".format(messaggio_byte[1], messaggio_byte[2],
                                messaggio_byte[3], messaggio_byte[4],
                                messaggio_byte[5])
    return {"tempo": tempo}
    #else:
    #    return {"tempo": "00:00"}
    
def team_scores(address, messaggio_byte):
    #0x82  =   130 [0x82] Team scores + Period + Bonus
    messaggio_byte = messaggio_byte.decode()
    left = "{}{}{}".format(messaggio_byte[0],messaggio_byte[1],messaggio_byte[2])
    right = "{}{}{}".format(messaggio_byte[3],messaggio_byte[4],messaggio_byte[5])
    period = "{}".format(messaggio_byte[7])
    return {"team_scoreL":left, "team_scoreR":right, "periodo":period}

def team_fouls(address, messaggio_byte):
    # [0x83] = 131 - Team Fouls + Player No. + Player Fouls
    messaggio_byte = messaggio_byte.decode()
    left = "{}{}".format( messaggio_byte[6], messaggio_byte[7])
    right = "{}{}".format( messaggio_byte[8], messaggio_byte[9])
    return {"falliL":left, "falliR":right}

def team_name_left(address, messaggio_byte):
    # [0x92] = 146  - Team Names (14 bytes)
    messaggio_byte = messaggio_byte.decode()
    name = "{}{}{}{}{}{}{}{}{}{}{}{}".format(messaggio_byte[0],messaggio_byte[1],messaggio_byte[2],messaggio_byte[3],
                                           messaggio_byte[4],messaggio_byte[5],messaggio_byte[6],
                                           messaggio_byte[7],messaggio_byte[8],messaggio_byte[9],
                                           messaggio_byte[10],messaggio_byte[11],)
    return {"team_left":name}


def team_name_right(address, messaggio_byte):
    # [0x93] = 147  - Team Names (14 bytes)
    messaggio_byte = messaggio_byte.decode()
    name = "{}{}{}{}{}{}{}{}{}{}{}{}".format(messaggio_byte[0],messaggio_byte[1],messaggio_byte[2],messaggio_byte[3],
                                           messaggio_byte[4],messaggio_byte[5],messaggio_byte[6],
                                           messaggio_byte[7],messaggio_byte[8],messaggio_byte[9],
                                           messaggio_byte[10],messaggio_byte[11],)
    return {"team_right":name}

def ser_dispo():
    """Stampa a video la lista delle seriali disponibili a sistema"""
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    print("-************************************************\n- Di seguito la lista delle seriali disponibili a sistema.\n-************************************************")
    porte = []
    for port, desc, hwid in sorted(ports):
            porte.append((port, desc))
            print("{}: {} [{}]".format(port, desc, hwid))
    ok_port="COM3"
    for el in porte:
        if  "USB-SERIAL CH340" in el[1]:
            ok_port = el[0]
            break
    
    print("\n- Il sistema ti propone {} Controlla che corrisponda a: USB-SERIAL CH340 e Conferma con INVIO la scelta".format(ok_port))
    scelta = input("Premi INVIO o immetti il nome della seriale -->")
    if scelta == '':
        nome_serial = ok_port
    elif (scelta,"USB-SERIAL CH340")  in porte:
        nome_serial = scelta
    return nome_serial


def controlla_copia():
    # CONTROLLO HD     ** Da completare **
    
    # Controllo che esista un file config.bin
    try:
        with open('config.bin','rb') as infile :
            dati = pickle.load(infile)
    except FileNotFoundError as er:
        print("mi dispiace ma questa copia non è autorizzata")
        pass     
    
    # leggo il seriale del HD
    f = os.popen('vol')
    s = f.read()
    s=s[s.index(":")+1:-1]
    print(s)

