'''def Temp(f):
    #função para transformar graus farenheit em celsius  
    C = (5 * (f - 32)/9)
    return C
f = int(input('Digite a temperatura:'))
celsius = Temp(f)
print('Temperatura em graus celsius: %d\n' %(celsius))
'''

'''quant = int(input('Digite o peso de peixes:'))
if( quant > 50):
    quant-=50
    print('João tem que pagar $50 + $%d de excesso.\n' %(4*quant))
else:
    print('Não houve excesso de peso!\n')'''


'''valor = float(input('Digite quanto você ganha por hora: '))
horas = int(input('Digite a quantidade de horas trabalhadas no mês :'))
salario = valor * horas
ir = (salario/100)*11
inss = (salario/100)*8
sindicato = (salario/100)*5
print('Salario bruto recebido: ', salario)
print('Descontos do salario:')
print('Imposto de renda: ', ir)
print('INSS: ', inss)
print('Sindicato: ', sindicato)
salario = salario-ir-inss-sindicato
print('Salario liquido: \n', salario)'''


'''litros = float(input('Digite a quantidade de litros:'))
tipo = str(input('Digite A para Alcool e G para Gasolina:'))
if(tipo == 'A'):
    preco = 3.45* litros
    if(litros <= 20):
        print('O valor final será %.2f' %(preco - (preco/100)*3))
    else: 
        print('O valor final será %.2f' %(preco - (preco/100)*5))
    print('preco')
elif(tipo == 'G'):
    preco = 4.53 * litros
    if(litros <= 20):
        print('O valor final será %.2f' %(preco - (preco/100)*4))
    else:
        print('O valor final será %.2f' %(preco - (preco/100)*6))
else:
    ('Erro!')'''

'''one = int(input('Digite a base:'))
two = int(input('Digite o expoente:'))
i = 0
result = 1
while i != two:
    result = result * one
    i+=1
print(result)'''

'''num = int(input('Digite um número:'))
i = 0
result = 1
while num != 0:
    result = result * num
    num -= 1
print(result)'''

'''numero = 1
while(numero > 0):
    numero = int(input('Digite um numero:'))
    if(numero < 16):
        num = numero
        i = 0
        result = 1
        while num != 0:
            result = result * num
            num -= 1
        print(result)'''

'''tab = int(input('Montar a tabuada de:'))
inicio = int(input('Começar por:'))
fim = int(input('Terminar por:'))
print('Tabuada do %d começando por %d e terminando por %d:' %(tab, inicio, fim))
while(inicio <= fim):
    print(tab, '*', inicio, '=', tab*inicio)
    inicio += 1'''

'''quant = int(input('Digite a quantidade de numeros:'))
i = 0
one = 0
two = 1
soma = 0
if( quant > 2 or quant == 2):
    print(one)
    print(two)
elif(quant == 1):
    print(one)
while( i < quant-2):
    soma = one + two
    print(soma)
    one = two
    two = soma
    i+=1'''

