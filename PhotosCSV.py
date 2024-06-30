import os
import pandas as pd
import numpy as np

NameList = os.listdir(r'C:\Users\narek\Рабочий стол\boocsv')

ChangeNameList = []
for i in range(len(NameList)):
    NameList[i] = NameList[i].split('.')
    if NameList[i][1] == 'bmp':
        ChangeNameList.append(NameList[i][0])
        ChangeNameList[i] = ChangeNameList[i].replace('__','_')
        ChangeNameList[i] = ChangeNameList[i].split("_")
        ChangeNameList[i][4] = ChangeNameList[i][4].replace("n","")
        ChangeNameList[i][5] = ChangeNameList[i][5].replace("m","")


ClassIDdict = {
    'Clear':0,
    'Human': 1,
    'Car': 2,
    'Noise whit line': 3,
    'Random Noise': 4
    }


CSVfile = pd.DataFrame(
    {
        'Class': [i[0] for i in ChangeNameList],
        'DataSet':[j[1] for j in ChangeNameList],
        'Trajectory':[k[2] for k in ChangeNameList],
        'Tact':[f[3] for f in ChangeNameList],
        'n':[g[4] for g in ChangeNameList],
        'm':[h[5] for h in ChangeNameList],
        'ClassID': [ClassIDdict[i[0]] for i in ChangeNameList]
    }

)

print(CSVfile)



