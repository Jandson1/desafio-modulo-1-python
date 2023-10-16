#Importando o pandas
import pandas as pd

#Adicionando o arquivo
df_vacinados = pd.read_csv('vacinados.csv')

#Filtro da parte 1 do desafio
df_vacinados1 = df_vacinados.loc[(df_vacinados['sexo'] == 'FEMININO') & ((df_vacinados['raca_cor'] == 'PARDA')| (df_vacinados['raca_cor'] == 'PRETA')) & (df_vacinados['idade'] > 60)]

#Visualização dos resultados pedidos
print(df_vacinados1)

# Convertendo a coluna 'data_vacinacao' em objetos de data e hora
df_vacinados['data_vacinacao'] = pd.to_datetime(df_vacinados['data_vacinacao'])

#Filtro da parte 2 do desafio
df_vacinados2 = df_vacinados.loc[(df_vacinados['sexo'] == 'MASCULINO') & ((df_vacinados['data_vacinacao'].dt.month == 11)|((df_vacinados['data_vacinacao'].dt.month == 12)))]
print(df_vacinados2)

