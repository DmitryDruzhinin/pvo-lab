import pandas as pd
file = pd.read_csv('file.csv')
file['sum'] = file[file.columns].sum(axis=1)
