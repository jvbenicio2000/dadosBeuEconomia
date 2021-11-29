import pandas as pd
import numpy as np 
# arquivo=pd.DataFrame()
# arquivo.to_excel("dados.xlsx")
tabela=pd.read_excel("dados.xlsx")
df=pd.DataFrame(tabela)
# print(df.head())
# print(df.info())

df_retornos=df.pct_change()
print(df_retornos.info())