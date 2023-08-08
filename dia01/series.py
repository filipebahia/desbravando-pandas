# %%
import pandas as pd

#%%
# Isso é uma lista
idade = [31,33,2,29,60,58]
idade[0]

#%%
media = sum(idade)/len(idade)
media

#%%
s_idade = pd.Series(idade)
s_idade[1]

#%%
# Métodos das Séries
s_idade.mean()
variancia = s_idade.var()
des_pad = s_idade.std()
s_idade.describe()

#%%
# Filtrando elementos de uma série
nova_idade = []
for i in idade:
    if i>=30:
        nova_idade.append(i)
nova_idade

filtro = s_idade >= 30
filtro

s_idade[filtro]
s_idade[~filtro] # Negativa do filtro



