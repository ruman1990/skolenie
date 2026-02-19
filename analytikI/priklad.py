<<<<<<< HEAD
import pandas as pd

moje_cisla = [4, 7, 8]
moj_series = pd.Series(moje_cisla, index=["a", "b", "c"])
print(moj_series[0])
=======
STOP = {"TAA", "TAG", "TGA"}
E = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
acc = "NC_000913.3"  # E. coli K-12 MG1655 complete genome
params={"db":"nuccore","id":acc,"rettype":"fasta","retmode":"text"}

import requests

data = requests.get(E,params=params)
with open('Ecoli.txt','w',encoding='utf-8') as f:
    f.write(data.text)

seq = []
with open('Ecoli.txt','r',encoding='utf-8') as f:
    for line in f:
        if '>' in line:
            continue
        seq.append(line.strip())

import re
parts = re.split("|".join(STOP),data.text)
print(parts)

row = []

for x in parts:
    d = {}
    d['start'] = len(x)
    d['sekvencia'] = x
    d['pocetG'] = x.count('G')
    row.append(d)

import pandas as pd
df = pd.DataFrame(row)
print(df)


    
>>>>>>> 517bdd9f1f48a227ed70221f69bbcae184df8d29
