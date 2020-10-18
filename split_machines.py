import pandas as pd
from pathlib import Path

chunksize = 500
last_machine = ''
machines_path = 'machines'
Path(machines_path).mkdir(parents=True, exist_ok=True)
for chunk in pd.read_csv('machine_usage.csv', chunksize=chunksize, names=range(9)):
    for index, row in chunk.iterrows():
        machine = row[0]
        line = ','.join(str(x) for x in row) + '\n'
        if last_machine != machine:
            last_machine = machine
            f = open(fr'{machines_path}/{machine}.csv', "a")
        f.write(line)