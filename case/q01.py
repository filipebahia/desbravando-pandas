# 1. Podemos remover algum tipo de massa do cardápio? Qual o impacto dessa ação?


#%%
import pandas as pd

#%%
df_item_pedido = pd.read_csv("../data/item_pedido.csv")
df_item_pedido

#%%
df_produto = pd.read_csv("../data/produto.csv")
df_produto

#%%
filtro_massa = df_item_pedido['descTipoItem'] == 'massa'

df_massa = df_item_pedido[filtro_massa].merge(df_produto,how='left')
df_massa

#%%
df_group = (df_massa.groupby(by=['descItem'])['idPedido'].nunique().reset_index())
df_group

df_group['Representa(%)'] = df_group['idPedido'] / df_group['idPedido'].sum()
df_group

#%%
df_group = (df_massa.groupby(by=['descItem'])
            .agg({"idPedido":['nunique'],
                  "vlPreco":['sum']})
            .reset
df_group