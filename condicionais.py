#  Created by avivyh on 01/06/22.
#  Copyright © 2022  avivyh. All rights reserved.




#estudando condicionais 
#if, else elif
# a condição não precisa estar entre parenteses
# necessária identação!!!

if (1 > 2) :
    print('Expressão if verdadeira\n')
elif(2>3) :
    print('Expressão elif verdadeira\n')
else:
    print('Expressão else verdadeira\n')

#verificando se é igual
if 5 == 5:
    print('TRUE\n')

idade = 18
if (idade>17):
    print('Você pode dirigir!\n')
    print('')
else:
    print('Espere mais um pouco amigo!\n')
    print('')

nome = 'Bob'

if(idade > 16):
    if nome == 'Bob':
        print('Você pode acessar!\n')
    else:
        print('Você não pode acessar!\n')


print("new\n")

# No AND as duas condições precisam ser verdadeiras para funcionarem
if(idade>16) and (nome == 'Bab'):
    print('And: Você pode acessar!\n')
else:
        print('And: Você não pode acessar!\n')

#No OR pelo menos um dos lados precisa ser verdadeiro para funcionar
if(idade>16) or (nome == 'Bab'):
    print('Or: Você pode acessar!\n')
else:
        print('Or: Você não pode acessar!\n')

#elif

dia = 'Terça'
if (dia == 'Segunda'):
    print('Hoje vai chover\n')
elif (dia == 'Terça'):
    print('Amanhã vai fazer sol\n')
else:
    print('Não sei a previsão ainda\n')


#solicitando dados do usuário

disciplina = input('Digite o nome da disciplina que você está pagando:\n')
notafinal = input('Digite a sua nota final:\n')
if(disciplina == 'Visão Computacional' and notafinal >= '7'):
    print('Você foi aprovado em visão computacional!\n')
elif(notafinal >= '7'):
    print('Você foi aprovado em', disciplina)
else:
    print('Você foi reprovado!\n')

disciplina = input('Digite a disciplina:')
notafinal = input('Digite a nota final:')
semestre = input('Digite o semestre:')

if (disciplina == 'Geografia') and (notafinal >= '80') and int(semestre != 1):
    print('Parabens! Você foi aprovado em %s com média final %r!' %(disciplina, notafinal))
elif(notafinal >= '70') and (semestre > '1'):
    print('Bem vindo, continue com seu desempenho\n')
else:
    print('Tente novamente no proximo semestre!')