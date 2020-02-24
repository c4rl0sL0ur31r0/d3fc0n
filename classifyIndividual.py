import csv
import pandas as pd

AloneData = pd.DataFrame()

LW = ['Anti-Police extremists','Anti-Gun Control extremists','Left-wing extremists']
ANAR = ['Anarchists']
IND = ['Separatists','Armenian nationalists']
NL = ['Anti-Technology extremists']
COMM = ['Marxist']
ENV = ['Animal Rights extremists']
SUPR = ['Anti-Semitic extremists','Ku Klux Klan','Anti-Immigrant extremists','White supremacists/nationalists','Anti-LGBT extremists','Anti-Muslim extremists']
NeoNz = ['Anti-Semitic extremists','Neo-Nazi extremists','Neo-Fascist extremists','Anti-Communist extremists','White supremacists/nationalists','Anti-LGBT extremists','Anti-Muslim extremists']
ED =['Right-wing extremists','Anti-Immigrant extremists','Anti-Communist extremists']
JI = ['Islamic State of Iraq and the Levant (ISIL)','Muslim extremists','Jihadi-inspired extremists','Hamas (Islamic Resistance Movement)','Jund Ansar Allah','Al-Shabaab']
REL = ['Supporters of Charles Manson','Anti-Christian extremists']

with open('alone.csv') as f:
    data = csv.DictReader(f)
    DataAppend = []
    for df in data:

        df['Anarquista'] = 0
        df['Animalista'] = 0
        df['Comunista'] = 0
        df['AntiFascista'] = 0
        df['ExtIzquierda'] = 0
        df['ExtDerecha'] = 0
        df['Independentista'] = 0
        df['Jihad'] = 0
        df['NeoLudita'] = 0
        df['NeoNazi'] = 0
        df['Religioso'] = 0
        df['Supremacista'] = 0

        if df['gname'] in LW:
            df['ExtIzquierda'] = 1

        if df['gname'] in ANAR:
            df['Anarquista'] = 1

        if df['gname'] in IND:
            df['Independentista'] = 1

        if df['gname'] in NL:
            df['NeoLudita'] = 1

        if df['gname'] in COMM:
            df['Comunista'] = 1

        if df['gname'] in ENV:
            df['Animalista'] = 1

        if df['gname'] in SUPR:
            df['Supremacista'] = 1

        if df['gname'] in NeoNz:
            df['NeoNazi'] = 1

        if df['gname'] in ED:
            df['ExtDerecha'] = 1

        if df['gname'] in JI:
            df['Jihad'] = 1
            df['Religioso'] = 1

        if df['gname'] in REL:
            df['Religioso'] = 1

        DataAppend.append(df)

newData = AloneData.append(DataAppend,ignore_index=True)
newData.to_excel('individual.xlsx')
print('*** Finished ***')
