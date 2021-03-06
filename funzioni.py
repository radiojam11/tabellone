# TecnoGeppetto 2022
# Contiene le funzioni  che fanno il parsing e compongono il messaggio
# 
import pickle, os

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
    try:
        messaggio_byte = messaggio_byte.decode()
    except UnicodeDecodeError:
        return {}
    tempo = "{}{}{}{}{}".format(messaggio_byte[1], messaggio_byte[2],
                                messaggio_byte[3], messaggio_byte[4],
                                messaggio_byte[5])
    return {"tempo": tempo}
    #else:
    #    return {"tempo": "00:00"}
    
def team_scores(address, messaggio_byte):
    #0x82  =   130 [0x82] Team scores + Period + Bonus
    try:
        messaggio_byte = messaggio_byte.decode()
    except UnicodeDecodeError:
        return {}
    left = "{}{}{}".format(messaggio_byte[0],messaggio_byte[1],messaggio_byte[2])
    right = "{}{}{}".format(messaggio_byte[3],messaggio_byte[4],messaggio_byte[5])
    period = "{}".format(messaggio_byte[7])
    return {"team_scoreL":left, "team_scoreR":right, "periodo":period}

def team_fouls(address, messaggio_byte):
    # [0x83] = 131 - Team Fouls + Player No. + Player Fouls
    try:
        messaggio_byte = messaggio_byte.decode()
    except UnicodeDecodeError:
        return {}
    left = "{}{}".format( messaggio_byte[6], messaggio_byte[7])
    right = "{}{}".format( messaggio_byte[8], messaggio_byte[9])
    return {"falliL":left, "falliR":right}

def team_name_left(address, messaggio_byte):
    # [0x92] = 146  - Team Names (14 bytes)
    try:
        messaggio_byte = messaggio_byte.decode()
    except UnicodeDecodeError:
        return {}
    name = "{}{}{}{}{}{}{}{}{}{}{}{}".format(messaggio_byte[0],messaggio_byte[1],messaggio_byte[2],messaggio_byte[3],
                                           messaggio_byte[4],messaggio_byte[5],messaggio_byte[6],
                                           messaggio_byte[7],messaggio_byte[8],messaggio_byte[9],
                                           messaggio_byte[10],messaggio_byte[11],)
    return {"team_left":name}


def team_name_right(address, messaggio_byte):
    # [0x93] = 147  - Team Names (14 bytes)
    try:
        messaggio_byte = messaggio_byte.decode()
    except UnicodeDecodeError:
        return {}
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
    if not len(porte):  # se non ci sono seriali collegate
        ok_port="NO PORT"
    for el in porte:        # per ogni porta trovata
        if  "USB-SERIAL CH340" in el[1]:        # se la descrizione della porta ?? quella corretta
            ok_port = el[0]
            break
    
    print("\n- Il sistema ti propone {} Controlla che corrisponda a: USB-SERIAL CH340 e Conferma con INVIO la scelta".format(ok_port))
    scelta = input("Premi INVIO o immetti il nome della seriale -->")
    if scelta == '':
        nome_serial = ok_port
    elif (scelta,"USB-SERIAL CH340")  in porte:     # se la scelta ?? tra le porte collegate...
        nome_serial = scelta
    else:                                           # se la scelta non ?? tra le porte collegate alza una eccezione ed esci 
        print("***********LA PORTA SERIALE SCELTA NON ?? RICONOSCIUTA***********")
        raise Exception("Sorry, EXIT")
    if nome_serial == "NO PORT":
        raise Exception("Sorry, NON RISULTA COLLEGATA LA SERIALE CORRETTA  EXIT")
    return nome_serial



def controlla_copia():
    # CONTROLLO HD     ** Da completare **
    
    # Controllo che esista un file config.bin
    try:
        with open('config.bin','rb') as infile :
            conf = pickle.load(infile)
    except FileNotFoundError:
        print("mi dispiace ma questa copia non ?? autorizzata")
        input("premi INVIO per continuare")
        raise NameError('No configuration file found!')     
    except EOFError :
        print("mi dispiace file di configurazione non corretto")
        input("premi INVIO per continuare")
        raise NameError('File di configurazione non corretto!')   
    # leggo il seriale del HD
    f = os.popen('vol')
    s = f.read()
    s=s[s.index(":")+1:-1]
    if s != conf:
        raise NameError('Copia non autorizzata!')
    print('programma regolare grazie!')
    return True

