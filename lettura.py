"""
Indirizza da manuale:

[0x80] Game clock + Possession + Timeout
[0x81] Shot clock + Timeout
[0x82] Team scores + Period + Bonus
[0x83] Team Fouls + Player No. + Player Fouls

[0x84..0x8D] Player No. + Penalty Time
        5 Left Penalties: 132 ÷ 136 (84hex ÷ 88hex).
        5 Right Penalties: 137 ÷ 141 (89hex ÷ 8Dhex).

[0x8E..0x91] Set scores
        Set 1  142 (8Ehex)
        Set 2  143 (8Fhex)
        Set 3  144 (90hex)
        Set 4  154 (91hex)

[0x92-0x93] Team Names (14 bytes)
        2. Left team  146 (92hex).
        3. Right team  147 (93hex).

[0x94] Horns
[0x95] Time of the day

[0x96] High resolution chonometer (14 bytes)

[0xA0..0xBE] Player Names (14 bytes)
        14 Left Players  160 ÷ 174 (A0hex ÷ AEhex).
        14 Right Players  176 ÷ 190 (B0hex ÷ BEhex).


[0xC0..0xDE] Player No. + Fouls+ Points + On-field status
        14 Left Players  192 ÷ 206 (C0hex ÷ CEhex).
        14 Right Players  208 ÷ 222 (D0hex ÷ DEhex).

[0xF0] Scoreboard brightness and sport


"""



import serial
from hexdump import hexdump
import pickle

address={0x80:("game_clock", 12), 0x81:("shot_clock", 12), 0x82:("team_scores", 12), 0x83:("team_fouls", 12), 
         0x84:("left_penality1", 12), 0x85:("left_penality2", 12), 0x86:("left_penality3", 12), 0x87:("left_penality4", 12), 
         0x88:("left_penality5", 12), 0x89:("right_penality1", 12),0x8A:("right_penality2", 12), 0x8B:("right_penality3", 12),
         0x8C:("right_penality4", 12), 0x8D:("right_penality5", 12),0x8E:("set1_score", 12), 0x8F:("setg2_score", 12),
         0x90:("set3_Score", 12), 0x91:("set4_score", 12),0x92:("team_name_left", 14), 0x93:("team_name_right", 14),0x94:("horns", 12),
         0x95:("time_of_the_day", 12),0x96:("hi_res_chrono", 12), 0xA0:("left_player1", 14),0xA1:("left_player2", 14), 
         0xA2:("left_player3", 14),0xA3:("left_player4", 14), 0xA4:("left_player5", 14),0xA5:("left_player6", 14),
         0xA6:("left_player7", 14),0xA7:("left_player8", 14), 0xA8:("left_player9", 14),0xA9:("left_player10", 14),
         0xAA:("left_player11", 14), 0xAB:("left_player12", 14),0xAC:("left_player13", 14),0xAD:("left_player14", 14), 
         0xAE:("left_player15", 14),
         0xB0:("right_player1", 14),0xB1:("right_player2", 14), 0xB2:("right_player3", 14),0xB3:("right_player4", 14),
         0xB4:("right_player5", 14), 
         0xB5:("right_player6", 12),0xB6:("right_player7", 14),0xB7:("right_player8", 14), 0xB8:("right_player9", 14),
         0xB9:("right_player10", 14),
         0xBA:("right_player11", 14), 0xBB:("right_player12", 14),0xBC:("right_player13", 14),0xBD:("right_player14", 14), 
         0xBE:("right_player15", 14),
         0xC0:("left_player1_fauls_point", 12),0xC1:("left_player2_fauls_point", 12), 0xC2:("left_player3_fauls_point", 12),
         0xC3:("left_player4_fauls_point", 12),
         0xC4:("left_player5_fauls_point", 12), 0xC5:("left_player6_fauls_point", 12), 0xC6:("left_player7_fauls_point", 12), 
         0xC7:("left_player8_fauls_point", 12),
         0xC8:("left_player9_fauls_point", 12), 0xC9:("left_player10_fauls_point", 12),0xCA:("left_player11_fauls_point", 12), 
         0xCB:("left_player12_fauls_point", 12), 
         0xCC:("left_player13_fauls_point", 12), 0xCD:("left_player14_fauls_point", 12),0xCE:("left_player15_fauls_point", 12), 
         0xD0:("right_player1_fouls_point", 12), 
         0xD1:("right_player2_fouls_point", 12), 0xD2:("right_player3_fouls_point", 12), 0xD3:("right_player4_fouls_point", 12), 
         0xD4:("right_player5_fouls_point", 12),
         0xD5:("right_player6_fouls_point", 12), 0xD6:("right_player7_fouls_point", 12),0xD7:("right_player8_fouls_point", 12), 
         0xD8:("right_player9_fouls_point", 12),
         0xD9:("right_player10_fouls_point", 12), 0xDA:("right_player11_fouls_point", 12),0xDB:("right_player12_fouls_point", 12), 
         0xDC:("right_player13_fouls_point", 12),
         0xDD:("right_player14_fouls_point", 12), 0xDE:("right_player5_fouls_point", 12), 0xF0:("scoreboard_brigtness_sport", 12)}

#RICORDATI DI SISTEMARE IL NOME DELLA SERIALE CON QUELLO CORRETTO

with serial.Serial('COM5', baudrate=19200, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_ODD  , timeout=15) as ser:
        print("inizializzata la seriale")
        raw = []
        while True:
                indirizzo_ricevuto = ser.read()          # read one byte
                """
                if indirizzo_ricevuto not in address.keys():   # se non e' un indirizzo conosciuto ritorna a leggere
                        print("non riconosco il pacchetto come indirizzo")
                        continue
                """
                print("ho BECCATO indirizzo")
                # se siamo qui abbiamo ricevuto uun indirizzo valido, quindi adesso vediamo quanti byte dobbiamo prendere
                #nome, packet_length = address[indirizzo_ricevuto]
                # adesso prendiamo tutti i byte del messaggio insieme nella variabile payload_ricevuto
                payload_ricevuto = ser.read()
                # prendo a parte il codice di controllo per fare poi le verifiche
                #lrc = ser.read()
                # e stampo un hexdump di quello che ho ricevuto
                #print(f"Printing hexdump for {nome}, per indirizzo: {indirizzo_ricevuto}")
                hexdump(payload_ricevuto)
                #hexdump(lrc)
                # salvo la lista dei messaggi ricevuti sul file
                raw.append(indirizzo_ricevuto)
                #raw.append(payload_ricevuto)
                #raw.append(lrc)
                file = open('dati.bin', 'wb')
                pickle.dump(raw, file)
                file.close()


        


""" 
    A="testaaawewqeqwewqeq\x00\x00".encode()    encode codifica in binario
    hexdump(A)  A e' una stringa e hexedump mi rende la visualizzazione in esadecimale della stringa binaria
 936 & 0b01111111  da applicare  al numero ricavato dalla somma per prendere solo gli ultimi due 
 NUMERO & 0b01111111   LO 0 A DX DEL b PORTA A ZERO LA CIFRA CHE TROVA NEL NUMERO MENTRE GLI 1 LA LASCIANO DEL SUO VALORE (SOMMA AND LOGICO)
 LA QUANTITA DEI NUMERI A DX DEL b CORRISPONDE ALLA QUANTITA DEI NUMERI PRESI NI CONSIDERAZIONE

int.from_bytes(b'\x34','big') == 0x34 == 52 == ord('4') != 4

>>> payload = B'PLAYERNAME'     
>>> t = 0xba
>>> for c in payload: 
...   t+=c            
... 

>>> t
936
>>> t & 0b01111111
40
>>> payload
b'PLAYERNAME'
>>> b'\xba'+payload 
b'\xbaPLAYERNAME'


«
    
"""            
        