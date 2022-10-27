from importlib.resources import path
import pandas as pd
import numpy as np
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'es_ES') #Es necesario con "_", no con "-"
import Modulos.database as db
from pathlib import Path

initialDate = input('Ingrese fecha inicial en formato YYYYMMDD: ')
finalDate = input('Ingrese fecha final en formato YYYYMMDD: ')
mes = datetime.strptime(initialDate,"%Y%m%d").strftime("%B")
initialDay = datetime.strptime(initialDate,"%Y%m%d").strftime("%d")
finalDay = datetime.strptime(finalDate,"%Y%m%d").strftime("%d")
anio = datetime.strptime(finalDate,"%Y%m%d").strftime("%Y")
FileName = mes + ' ' + anio + ' (' + initialDay + ' - ' + finalDay + ').xlsx'

typeBilling = input('Escriba M si es facturación mensual y S si es semanal: ').upper()
if typeBilling == 'S':
	semana = input('Ingrese el número de semana: ')
	FileName = mes + ' ' + anio + ' semana ' + semana + ' (' + initialDay + ' - ' + finalDay + ').xlsx'

print('Realizando extracción de datos')
billing = db.extractbilling(typeBilling, initialDate, finalDate)

print('Generando informes en excel')
billing[(billing.Alias == 'Latam CL')].to_excel(Path('Output', 'LATAM CL - ' + FileName), index = False)
billing[(billing.Alias == 'Latam PE')].to_excel(Path('Output', 'LATAM PE - ' + FileName), index = False)
billing[(billing.Alias == 'Latam EC')].to_excel(Path('Output', 'LATAM EC - ' + FileName), index = False)
billing[(billing.Alias == 'Latam CO')].to_excel(Path('Output', 'LATAM CO - ' + FileName), index = False)

print('Extracción de datos realizada')