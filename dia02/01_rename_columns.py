#%%
import pandas as pd

#%%
df = pd.read_csv("../data/pedido.csv")
df

#%%
df.rename(columns={'descUF': 'descEstado'})

#%%
df = df.rename(columns={'descUF': 'descEstado'})

#%%
df.rename(columns={'descUF': 'descEstado'}, inplace=True)