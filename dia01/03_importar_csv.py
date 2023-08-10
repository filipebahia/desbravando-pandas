#%%
import pandas as pd

#%%
df = pd.read_csv('../data/pedido.csv')
df

#%%
df.columns

#%%
df.shape

#%%
df.types

#%%
df.head()

#%%
df.tail()

#%%
df.sample()