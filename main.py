import pandas as pd

file_path = '/kaggle/input/datacon24-main/DataCon24-main/Datasets/Mixed CPPs/POSEIDON.csv'
df = pd.read_csv(file_path, sep=',', encoding='unicode_escape', on_bad_lines='skip')

print(df.head())