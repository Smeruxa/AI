M = [[0 for _ in range(N_items)] for _ in range(N_users)]

for i in range(len(df_data)):
  user_id = df_data.iloc[i]['user_id']
  item_id = df_data.iloc[i]['item_id']
  M[user_id][item_id] = df_data.iloc[i]['rating']
