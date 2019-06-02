# -*- coding: utf-8 -*-
import string

def maiusculas(a_string):
    uppers = ""
    for c in a_string:
        if c in string.ascii_uppercase:
            uppers = uppers + c
    return uppers

print(maiusculas('Programamos em python 2?'))
# deve devolver 'P'
print(maiusculas('Programamos em Python 3.'))
# deve devolver 'PP'
print(maiusculas('PrOgRaMaMoS em python!'))
# deve devolver 'PORMMS'
