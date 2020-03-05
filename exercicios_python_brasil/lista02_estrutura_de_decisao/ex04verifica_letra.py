'''
04. Faça um Programa que verifique se uma letra digitada é vogal ou consoante
'''
letra = str(input('digite uma letra: ')).upper()

if letra in 'AEIOU':
    print('A letra digitada é uma VOGAL!')
else:
    print('A letra digitada é uma CONSOANTE!')