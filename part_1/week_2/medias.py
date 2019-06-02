# -*- coding: utf-8 -*-
posicoes = ["primeira", "segunda", "terceira", "quarta"]
notas = []
soma = 0.0

for i in range(0, 4): 
	nota = float(input('Digite a %s nota: ' % posicoes[i]))
	notas.append(nota)
	soma = soma + notas[i]

print("A média aritmética é %.2f" % (soma / 4))
