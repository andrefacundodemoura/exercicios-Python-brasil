# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = int(input('Quantos MB tem o arquivo a ser baixado? \n'))
link = int(input('Qual a velocidade do seu link (mbps)?\n'))

tempo = arquivo / link
minutos=tempo/60

if minutos < 1:
    tempo=int(float(tempo))
    print(f'Tempo para download {tempo} segundos.')
else:
    minutos = int(float(minutos))
    print(f'Tempo para download {minutos} minutos e {tempo % link :.0f} segundos.')

