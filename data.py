#  Created by avivyh on 17/06/22.
#  Copyright © 2022  avivyh. All rights reserved.

#ps: NUNCA colocar o nome do arquivo datetime.py na pasta do projeto
import datetime
#passando a hora atual p variavel agora, usando o método datetime do módulo date time 
#informa a data atual, ano, mes, dia, hora, minuto, segundo e milisegundo.
agora = datetime.datetime.now()
print(agora)
print('')

#criando a propria data
t = datetime.time(7, 43, 28)
print(t)
print('')

#extraindo hora
print('Hora:', t.hour)
#extraindo minuto
print('Minutos:', t.minute)
#extraindo segundos 
print('Segundos:', t.second)
#extraindo microsegundos
print('Microsegundos:', t.microsecond)
print('')

print(datetime.time.min)
print('')

#extraindo a data de hoje
hoje = datetime.date.today()
print(hoje)
print('Ctime:', hoje.ctime())
print('Ano:', hoje.year)
print('Mês:', hoje.month)
print('Dia:', hoje.day)
print('')

#calculos com datas 
date1 = datetime.date(2015, 4, 28)
print('Primeira data: ', date1)
date2 = date1.replace(year=2016)
print('Segunda data: ', date2)
print('')

#Diferença entre as duas datas 
print(date2 - date1)