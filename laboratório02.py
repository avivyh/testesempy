#imprimindo o menu para o usuário
print('*********************************** PYTHON CALCULADORA ***********************************\n')
print('Selecione o número da operação desejada:\n')
print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n')
#solicitando a operação a ser realizada
operação = int(input('Digite o número correspondente a operação: (1/2/3/4)\n'))
print('')
#solicitando valores
x = int(input('Digite o primeiro número:\n'))
y = int(input('Digite o segundo número:\n'))
print('')
#opções de operações
#chamando a função anonima lambda para solucionar as operações e imprimindo o resultado
#ps: sempre passar os argumentos da variavel que vai receber o valor de lambda!!!
if(operação == 1):
    result = lambda x, y: x+y
    print(x, '+', y, '=', result(x, y))
elif(operação == 2):
    result = lambda x, y: x-y
    print(x, '-' , y, '=', result(x, y))
elif(operação == 3):
    result = lambda x, y: x*y
    print(x, '*' , y, '=', result(x, y))
elif(operação == 4):
    result = lambda x, y: x/y
    print(x, '/' , y, '=', result(x, y))
else:
    print('Operação não reconhecida!')
print('')