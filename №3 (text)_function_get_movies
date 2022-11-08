# находит пользователя user2, который похож на user1 и ВСЕ ФИЛЬМЫ, которые смотрел user2 и не смотрел user1
def get_movies(user1, M):
  max = 0
  user_max = None
  for user2 in M:
    value = cosine(user1, user2)
    if value > max and user1 != user2:
      max = value
      user_max = user2
  
  movies = []
  for i in range(len(user_max)):
    if user1[i] == 0 and user_max[i] > 3:
      movies.append(i)
  return movies, max, user_max
