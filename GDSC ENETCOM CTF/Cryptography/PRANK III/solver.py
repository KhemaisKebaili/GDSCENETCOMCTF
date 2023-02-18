import base64
import validators
import re

encoded_string_part1="NB2HI4DTHIXS64DBON2GKYTJNYXGG33NF5WUOQSVJBT"
encoded_string_part2="WA="

b32="ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
for i in range(32):
    for j in range(32):
        r = encoded_string_part1+b32[i]+b32[j]+encoded_string_part2
        decoded=base64.b32decode(r)
        print(decoded)
        
