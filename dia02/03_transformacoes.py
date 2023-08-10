#%%
import pandas as pd
import numpy as np

#%%
df = pd.read_csv("../data/produto.csv")
df

#%%
df.info()

#%%
df['precoAjustado'] = df['vlPreco']
df

#%%
df['precoAjustado'] = df['vlPreco'] * 1.09
df

#%%
df['precoAjustado'] = df['precoAjustado'].round(2)
df

#%%
df['txAjuste(%)'] = (100 * (df['precoAjustado'] / df['vlPreco'] - 1)).round(2)
df['txAjuste(%)']

#%%
df = df.drop(columns = ['txAjuste'])
df

#%%
del df['txAjuste']
df

#%%
df['txAjuste(%)']

#%%
np.log([2.14,10])

#%%
df['logTxAjuste'] = np.log(df['txAjuste(%)'])
df

#%%
df['expTxAjuste'] = np.exp(df['txAjuste(%)'])
df

#%%
def fatorial(x):
    total = 1
    for i in range(2,int(x)+1):
        total *= i
    return total

fatorial(5)
# %%
df['precoAjustado'].apply(fatorial)