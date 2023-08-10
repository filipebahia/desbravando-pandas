#%%
import pandas as pd

#%%
data = {
    "nome":["Teo", "Nah", "Maria", "José", "Marina"],
    "idade":[30,20,12,44,53],
    "cor":["Preto", "Azul", "Verde","Vermelho","Amarelo"],
    "renda":[3450,2342,5678,4432,10800]
}

df = pd.DataFrame(data)
df["idade"]

#%%
type(df["idade"])
type(data["idade"])

#%%
df.mean()

#%%
df.describe()
df[['idade','renda']].describe()
#teste