import pandas as pd
file = pd.read_csv('csv.csv')
file['sum'] = file[file.columns].sum(axis=1)