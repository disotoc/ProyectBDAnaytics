import pandas as pd
import numpy as np
from pathlib import Path
import Modulos.database as db

initialDate = '20220701'
FileNameJustification = 'Justificaciones.xlsx'
FileNameCNA = 'ReporteCNA.xlsx'

print('Realizando extraccion de datos')
db.extractJustification().to_excel(Path('Output', FileNameJustification), index = False)
db.extractCNAReport(initialDate).to_excel(Path('Output', FileNameCNA), index = False)

print('Exportación finalizada')