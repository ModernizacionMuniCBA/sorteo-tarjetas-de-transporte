#!/usr/bin/python3

'''
Script para sortear tarjetas de transporte con crédito sobre la lista de viajantes de un día específico.

'''
import csv
import subprocess
import random

premios_a_entregar = 10

data_file = 'sample-data.csv'

# muestra de datos
'''
NROEXTERNO', 'NROINTERNO', 'DNI', 'FECHA', 'HORA', 'LINEA', 'EMPRESA
111111', '111111111111', '', '19/09/2017', '06:00:00 AM', 'L67', 'Coniferal S.A.C.I.F.
222222', '222222222222', '', '19/09/2017', '06:00:00 AM', 'L17', 'Coniferal S.A.C.I.F.
333333', '333333333333', '', '19/09/2017', '06:00:01 AM', 'L25', 'ERSA
444444', '444444444444', '', '19/09/2017', '06:00:01 AM', 'L73', 'ERSA

- Nro de serie externo de la tarjeta
- Nro. de serie interno de la tarjeta
- DNI (en blanco en caso de tarjeta no registrada)
- Fecha  TRX
- Hora TRX
- Línea
- Empresa
'''

print('Contando líneas ...')

res = subprocess.check_output(['wc', '-l', data_file])
lineas = int(res.decode('utf-8').split()[0]) - 1

print('{} líneas encontradas'.format(lineas))
print('{} premios a entregar'.format(premios_a_entregar))

ganadores = []
for i in range(1, premios_a_entregar + 1):
    rand = random.random()
    ganador = int(round(rand * lineas, 0))

    while ganador in ganadores:  # evitar duplicado
        rand = random.random()
        ganador = int(round(rand * lineas, 0))
        # print('{}: {}'.format(i, ganador))
    ganadores.append(ganador)

ganadores = sorted(ganadores)

headers = ['NROEXTERNO', 'NROINTERNO', 'DNI', 'FECHA', 'HORA', 'LINEA', 'EMPRESA']

ganadores_final = []
ganadores_count = 0
with open(data_file, encoding='iso-8859-1') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    file_headers = next(reader)
    print(file_headers)
    c = 1
    for row in reader:
        pass
        if c in ganadores:
            ganadores_count += 1
            print('**********\n#{} Ganador NUMERO {}/{}'.format(ganadores_count, c, lineas))
            print('Externo: {} Interno:{} DNI:{} FECHA:{} {} Linea:{} Empresa:{}'.format(row['NROEXTERNO'], row['NROINTERNO'], row['DNI'], row['FECHA'], row['HORA'], row['LINEA'], row['EMPRESA']))
        c+= 1

