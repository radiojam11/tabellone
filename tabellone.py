"""
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
parity=serial.PARITY_EVEN, rtscts=1

import serial
address={"0x80":"game_clock", "0x81":"shot_clock", "0x82":"team_scores", "0x83":"team_fouls", 
         "0x84":"left_penality1", "0x85":"left_penality2", "0x86":"left_penality3", "0x87":"left_penality4", 
         "0x88":"left_penality5", "0x89":"right_penality1","0x8A":"right_penality2", "0x8B":"right_penality3",
         "0x8C":"right_penality4", "0x8D":"right_penality5","0x8E":"set1_score", "0x8F":"setg2_score",
         "0x90":"set3_Score", "0x91":"set4_score","0x92":"team_name_left", "0x93":"team_name_right","0x94":"horns",
         "0x95":"time_of_the_day","0x96":"hi_res_chrono", "0xA0":"left_player1","0xA1":"left_player2", 
         "0xA2":"left_player3","0xA3":"left_player4", "0xA4":"left_player5","0xA5":"left_player6",
         "0xA6":"left_player7","0xA7":"left_player8", "0xA8":"left_player9","0xA9":"left_player10",
         "0xAA":"left_player11", "0xAB":"left_player12","0xAC":"left_player13","0xAD":"left_player14", "":"","":"","":"", "":"","":"","":"", "":"","":"","":"", "":"","":"","":"", "":"","":"","":"", "":"","":"","":"", "":"","":"","":"", "":"",
         "":"", "":"","":"", "":"","":"", "":"",}
with serial.Serial('/dev/ttyS1', baudrate=19200, bytesize="EIGHTBITS", stopbits="STOPBITS_ONE", parity="PARITY_ODD",timeout=1) as ser:
  x = ser.read()          # read one byte
  
