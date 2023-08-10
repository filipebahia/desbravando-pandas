#%%
import pandas as pd

#%%
df = pd.read_csv('../data/pedido.csv')
df

#%%
df[["descUF","txtRecado"]]

#%%
colunas = ["idPedido", "flKetchup"]
df[colunas]


#%%
colunas = ['idPedido', 'descUF', 'dtPedido', 'txtRecado', 'flKetchup']
df[colunas]

#%%
df = df[colunas]
df

#%%
df_sample = df.sample(100)
df_sample

#%%
# iloc pega a posição e não o índice
df_sample.iloc[0]

df_sample.iloc[[0,2,5]]

df_sample.iloc[:3]

df.loc[1:100]

df.iloc[1:10]['idPedido']

