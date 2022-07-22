import pandas as pd
import numpy as np
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'es_ES')

dropship = pd.read_excel('ExcelFiles\Dropship.xlsx')
dropship['Día de Order Date'] = dropship['Día de Order Date'].apply(lambda self: datetime.strptime(self,"%d de %B de %Y")).astype('datetime64[ns]')
dropship['Día de Po Date'] = dropship['Día de Po Date'].apply(lambda self: datetime.strptime(self,"%d de %B de %Y")).astype('datetime64[ns]')
dropship["Po Item Sku"] = dropship["Po Item Sku"].str.replace("|","").astype("string")
dropship["Po Item Sku"] = dropship["Po Item Sku"].str.replace("-EXPRESS","").astype("string")
dropship = dropship[(dropship.Client == 'Latam') | (dropship.Client == 'Latam CL') | (dropship.Client == 'Latam PE') | (dropship.Client == 'Latam CO')]
dropship = dropship.drop(['Record Number'], axis=1)
dropship = dropship[~dropship['Po Item Sku'].str.contains("sorteo", case=False)]
dropship.to_excel('BD_Analytics.xlsx', index = False)






