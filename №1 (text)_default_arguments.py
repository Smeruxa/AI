import pandas as pd

df_data = pd.read_csv("/content/Dataset.csv")
df_titles = pd.read_csv("/content/Movie_Id_Titles.csv")

def length(v):
  S = 0
  for i in range(len(v)):
    S += v[i]**2
  return S**(0.5)

def cosine(v, w):
  S = 0
  for i in range(len(v)):
    S += v[i]*w[i]
  return S/(length(v)*length(w))
  
df_data['user_id'].value_counts() # сколько какой пользователь встречается в данном столбце
df_data['user_id'].unique() # получить уникальные значение по данном столбцу

N_users = len(df_data['user_id'].unique()) + 1
N_items = len(df_data['item_id'].unique()) + 1

print(N_users, N_items)
