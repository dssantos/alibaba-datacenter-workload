import pandas as pd
from pathlib import Path

Path("machines/").mkdir(parents=True, exist_ok=True)

chunksize = 500
last_machine = ''
for chunk in pd.read_csv('machine_usage.csv', chunksize=chunksize, names=range(9)):
    for index, row in chunk.iterrows():
        machine = row[0]
        line = ','.join(str(x) for x in row) + '\n'
        if last_machine != machine:
            last_machine = machine
            f = open(f"machines/{machine}.csv", "a")
        f.write(line)