'''
12. Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita).
 O Salário Líquido corresponde ao Salário Bruto menos os descontos.
 O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''
preco = float(input('Digite o valor da hora trabalhada:R$'))
horas = int(input('Quantas horas trabalhadas: '))
tb = horas * preco
ir = 0
tir = 0
fgts = tb / 100 * 11
sind = tb / 100 * 3
inss = tb / 100 * 10
tdesc = ir + inss

if tb > 900 and tb <= 1500:
    tir = 5
    ir = tb /100 * tir
    tdesc = ir + inss
elif tb > 1500 and tb <= 2500:
    tir = 10
    ir = tb / 100 * tir
    tdesc = ir + inss
elif tb > 2500:
    tir = 20
    ir = tb / 100 * tir
    tdesc = ir + inss
print(f'''
        Salário Bruto: ({preco} * {horas})        : R${tb}
        (-) IR ({tir}%)                       : R${ir}
        (-) INSS ( 10%)                 : R${inss}
        FGTS (11%)                      : R${fgts}
        Sindicato(3%)                   : R${sind}
        Total de descontos              : R${tdesc}

        Salário Liquido                 : R${tb - tdesc}

''')