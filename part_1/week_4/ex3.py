# -*- coding: utf-8 -*-
n = int(input("Digite um número inteiro: "))
s = 0
while n:
    s += n % 10
    n //= 10 
print(s)