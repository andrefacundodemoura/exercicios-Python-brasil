'''
13. Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

OBS: Os dois blocos de codigo fazem o mesmo trabalho, porem o primeiro
de uma maneira intuitiva, e o segundo de maneira mais inteligente.
'''
# num = 0
# while num != 1 or 2 or 3 or 4 or 5 or 6 or 7:
#     num = int(input('digite o numero correspondente ao dia da semana: '))
#     if num in (1,2,3,4,5,6,7):
#         break
#     else:
#         print('valor digitado invalido')
# if num == 1:
#     num = 'domingo'
# elif num == 2:
#     num = 'segunda'
# elif num == 3:
#     num = 'terça'
# elif num == 4:
#     num = 'quarta'
# elif num == 5:
#     num = 'quinta'
# elif num == 6:
#     num = 'sexta'
# elif num == 7:
#     num = 'sabado'
#
# print(f'O numero digitado correspondente ao dia da semana: {num}')

#####################################################################################
num=0
dias = {1:'Domingo',2:'Segunda',3:'Terça',4:'Quarta',5:'Quinta',6:'Sexta',7:'Sabado'}

while num not in dias:
    num = int(input('Digite o numero correspondente ao dia da semana: '))
    if num in dias:
        print(f'O valor digitado corresponde ao dia da semana : {dias[num]}')
    else:
        print('Valor digitado invalido')
#####################################################################################