# TecnoGeppetto 2022
# Contiene le funzioni  che fanno il parsing e compongono il messaggio
# 
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

def controlla_copia():
    # CONTROLLO HD     ** Da completare **
    f = os.popen('vol')
    s = f.read()
    s=s[s.index(":")+1:-1]
    
    print(s)


def ser_dispo():
    """Stampa a video la lista delle seriali disponibili a sistema"""
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    print("\n\n-\nDi seguito la lista delle seriali disponibili a sistema.\n  -")
    for port, desc, hwid in sorted(ports):
            print("{}: {} [{}]".format(port, desc, hwid))