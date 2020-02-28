'''
14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
 de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
 de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
  João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
 Gravar na variável excesso a quantidade de quilos além do limite e na variável multa
  o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''

peso = float(input('''
Bom dia seo João espero que a pescaria tenha sido proveitosa. 
Digite aqui qntos kilos o senhor pegou:  
'''))

if peso > 50:
    sobra = peso - 50
    multa = sobra*4
    print(f'Infelismente o senhor excedeu o limite de 50KG de peixe em {sobra}KG ')
    print(f'O senhor tera que pagar uma multa de R${multa} mais cuidado da proxima vez.')

else:
    print(f' O peso informado ({peso}KG) esta dentro das normas.Parabéns pelo seu dia de trabalho')