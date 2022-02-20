# TecnoGeppetto 2022
# Contiene le funzioni  che fanno il parsing e compongono il messaggio
# 

def game_clock(address, messaggio_byte):
    # [0x80] = 128 Game clock + Possession + Timeout
    if messaggio_byte[0] == "G":
        # Chronometer is counting, game time    Address 0x80
        tempo = "{}{}{}{}{}".format(messaggio_byte[1], messaggio_byte[2],
                                    messaggio_byte[3], messaggio_byte[4],
                                    messaggio_byte[5])
        return {"tempo": tempo}
    else:
        return {"tempo": "00:00"}
    
def team_scores(address, messaggio_byte):
    #0x82  =   130 [0x82] Team scores + Period + Bonus
    left = "{}{}{}".format(messaggio_byte[0],messaggio_byte[1],messaggio_byte[2])
    right = "{}{}{}".format(messaggio_byte[3],messaggio_byte[4],messaggio_byte[5])
    return {"left":left, "right":right}

def team_fouls(address, messaggio_byte):
    # [0x83] = 131 - Team Fouls + Player No. + Player Fouls
    left = "{}{}".format( messaggio_byte[6], messaggio_byte[7])
    right = "{}{}".format( messaggio_byte[8], messaggio_byte[9])
    return {"left":left, "right":right}

def team_name_left(address, messaggio_byte):
    # [0x92] = 146  - Team Names (14 bytes)
    name = "{}{}{}{}{}{}{}{}{}{}{}".format(messaggio_byte[1],messaggio_byte[2],messaggio_byte[3],
                                           messaggio_byte[4],messaggio_byte[5],messaggio_byte[6],
                                           messaggio_byte[7],messaggio_byte[8],messaggio_byte[9],
                                           messaggio_byte[10],messaggio_byte[11],)
    return {"name":name}


def team_name_right(address, messaggio_byte):
    # [0x93] = 147  - Team Names (14 bytes)
    name = "{}{}{}{}{}{}{}{}{}{}{}".format(messaggio_byte[1],messaggio_byte[2],messaggio_byte[3],
                                           messaggio_byte[4],messaggio_byte[5],messaggio_byte[6],
                                           messaggio_byte[7],messaggio_byte[8],messaggio_byte[9],
                                           messaggio_byte[10],messaggio_byte[11],)
    return {"name":name}
