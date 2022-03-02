import pickle
from pyrsistent import b

address_ridotto = {
    b"\x80":("game_clock", 12),
    b"\x82":("team_scores", 12),
    b"\x83":("team_fouls", 12),
    b"\x92":("team_name_left", 14),
    b"\x93":("team_name_right", 14),
    b"\x96":("hi_res_chrono", 12)
    
}

address={b"\x80":("game_clock", 12),b"\x81":("shot_clock", 12), b"\x82":("team_scores", 12), b"\x83":("team_fouls", 12), 
         b"\x84":("left_penality1", 12), 
         b"\x85":("left_penality2", 12), b"\x86":("left_penality3", 12), b"\x87":("left_penality4", 12), 
         b"\x88":("left_penality5", 12), b"\x89":("right_penality1", 12),b"\x8A":("right_penality2", 12), b"\x8B":("right_penality3", 12),
         b"\x8C":("right_penality4", 12), "\x8D":("right_penality5", 12),"\x8E":("set1_score", 12), b"\x8F":("setg2_score", 12),
         b"\x90":("set3_Score", 12), b"\x91":("set4_score", 12),b"\x92":("team_name_left", 14), b"\x93":("team_name_right", 14),
         b"\x94":("horns", 12),
         b"\x95":("time_of_the_day", 12),b"\x96":("hi_res_chrono", 12), b"\xA0":("left_player1", 14),b"\xA1":("left_player2", 14), 
         b"\xA2":("left_player3", 14),b"\xA3":("left_player4", 14), b"\xA4":("left_player5", 14),b"\xA5":("left_player6", 14),
         b"\xA6":("left_player7", 14),b"\xA7":("left_player8", 14), b"\xA8":("left_player9", 14),b"\xA9":("left_player10", 14),
         b"\xAA":("left_player11", 14), b"\xAB":("left_player12", 14),b"\xAC":("left_player13", 14),b"\xAD":("left_player14", 14), 
         b"\xAE":("left_player15", 14),
         b"\xB0":("right_player1", 14),b"\xB1":("right_player2", 14), b"\xB2":("right_player3", 14),b"\xB3":("right_player4", 14),
         b"\xB4":("right_player5", 14), 
         b"\xB5":("right_player6", 12),b"\xB6":("right_player7", 14),b"\xB7":("right_player8", 14), b"\xB8":("right_player9", 14),
         b"\xB9":("right_player10", 14),
         b"\xBA":("right_player11", 14), b"\xBB":("right_player12", 14),b"\xBC":("right_player13", 14),b"\xBD":("right_player14", 14), 
         b"\xBE":("right_player15", 14),
         b"\xC0":("left_player1_fauls_point", 12),b"\xC1":("left_player2_fauls_point", 12), b"\xC2":("left_player3_fauls_point", 12),
         b"\xC3":("left_player4_fauls_point", 12),
         b"\xC4":("left_player5_fauls_point", 12), b"\xC5":("left_player6_fauls_point", 12), b"\xC6":("left_player7_fauls_point", 12), 
         b"\xC7":("left_player8_fauls_point", 12),
         b"\xC8":("left_player9_fauls_point", 12), b"\xC9":("left_player10_fauls_point", 12),b"\xCA":("left_player11_fauls_point", 12), 
         b"\xCB":("left_player12_fauls_point", 12), 
         b"\xCC":("left_player13_fauls_point", 12), b"\xCD":("left_player14_fauls_point", 12),b"\xCE":("left_player15_fauls_point", 12), 
         b"\xD0":("right_player1_fouls_point", 12), 
         b"\xD1":("right_player2_fouls_point", 12), b"\xD2":("right_player3_fouls_point", 12), b"\xD3":("right_player4_fouls_point", 12), 
         b"\xD4":("right_player5_fouls_point", 12),
         b"\xD5":("right_player6_fouls_point", 12), b"\xD6":("right_player7_fouls_point", 12),b"\xD7":("right_player8_fouls_point", 12), 
         b"\xD8":("right_player9_fouls_point", 12),
         b"\xD9":("right_player10_fouls_point", 12), b"\xDA":("right_player11_fouls_point", 12),b"\xDB":("right_player12_fouls_point", 12), 
         b"\xDC":("right_player13_fouls_point", 12),
         b"\xDD":("right_player14_fouls_point", 12), b"\xDE":("right_player5_fouls_point", 12), b"\xF0":("scoreboard_brigtness_sport", 12)}


infile = open('3dato.bin','rb')
dati = pickle.load(infile)
infile.close()
print(dati)
n = len(dati)
#print(n)
for i in range(n-1):
    el = dati.pop(0)
    #print(int.from_bytes(el, 'big'))
    if el not in address_ridotto.keys():
        continue
    if el == b'\xa2' :
        continue
    if  el == 0xa2 :
        continue
    ind, num_byte = address[el]
    payload_ricevuto = []
    for u in range(num_byte-1):
        el = dati.pop(0)
        payload_ricevuto.append(el)
    messaggio = ""
    if ind == "team_name_left":
        for el in payload_ricevuto[:-1]:
            messaggio +=  el.decode()
            #pass 
    #print(ind,payload_ricevuto)
        print(messaggio)
    #lrc = ser.read()

    #print(f"Printing hexdump for {nome}, per indirizzo: {indirizzo_ricevuto}")
    #hexdump(payload_ricevuto)