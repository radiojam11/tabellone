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
address={"game_clock":"0x80", "shot_clock":"0x81", "team_scores":"0x82" }
with serial.Serial('/dev/ttyS1', baudrate=19200, bytesize="EIGHTBITS", stopbits="STOPBITS_ONE", parity="PARITY_ODD",timeout=1) as ser:
  x = ser.read()          # read one byte
  
