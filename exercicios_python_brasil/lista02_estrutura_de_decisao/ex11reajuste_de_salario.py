'''
11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''
salario = float(input('Digite o valor do para calcular o novo salario:\n R$'))
almento =0
if salario <= 280:
    almento = salario / 100 * 20
    print(f'O salario antigo de R${salario} tera um almento de 20% (R${almento}) \nTOTAL:R${salario+almento}')
elif salario > 280 and salario <= 700:
    almento = salario / 100 * 15
    print(f'O salario antigo de R${salario} tera um almento de 15% (R${almento}) \nTOTAL:R${salario + almento}')
elif salario >700 and salario < 1500:
    almento = salario / 100 * 10
    print(f'O salario antigo de R${salario} tera um almento de 10% (R${almento}) \nTOTAL:R${salario + almento}')
elif salario >= 1500:
    almento = salario / 100 * 5
    print(f'O salario antigo de R${salario} tera um almento de 5% (R${almento}) \nTOTAL:R${salario + almento}')