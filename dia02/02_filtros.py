#%%
import pandas as pd

#%%
df = pd.read_csv("../data/pedido.csv")
df

#%%
idade = pd.Series([30,23,76,12,44,22,98])
filtro = idade > 40
idade[filtro]

#%%
filtro_uf = df['descUF'] == 'São Paulo'
df[filtro_uf]

#%%
filtro_sp_ketchup = (df['descUF']=='São Paulo') & (df['flKetchup'])
df[filtro_sp_ketchup]

#%%
filtro_ufs_ketchup = ((df['descUF']=='São Paulo') | (df['descUF']=='Rio de Janeiro') | (df['descUF']=='Paraná')) & df['flKetchup'] 
df[filtro_ufs_ketchup]

#%%
ufs = ['São Paulo','Rio de Janeiro','Paraná']
filtro_ufs_ketchup = df['descUF'].isin(ufs) & df['flKetchup']
df[filtro_ufs_ketchup]

#%%
filtro_txt_na = df['txtRecado'].isna()
df[filtro_txt_na]

#%%
df.isnull()
df['flKetchup'].isnull()

#%%
