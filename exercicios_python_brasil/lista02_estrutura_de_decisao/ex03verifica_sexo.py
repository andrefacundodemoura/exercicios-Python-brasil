'''
03. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
sexo = ''
while sexo != 'M' or 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    if sexo in 'MF':
        break
    else:
        print('sexo invalido.')
if sexo == 'M':
    print('sexo masculino')
elif sexo == 'F':
    print('sexo feminino.')
