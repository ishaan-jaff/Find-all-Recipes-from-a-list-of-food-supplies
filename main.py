from collections import defaultdict
def find_recipes(recipes, ingredients, supplies):
    # build adj list, in_degree, visited

  adj_list, in_degree, visited = defaultdict(list), defaultdict(int), defaultdict(bool)

  for i, elem in enumerate(recipes):
    ingredients_list = ingredients[i]
    for ingredient in ingredients_list:
      adj_list[ingredient].append(elem)
      in_degree[elem]+=1
      if ingredient not in in_degree:
        in_degree[ingredient] = 0

  print(adj_list)
  print(in_degree)

  # traverse adj list 
  q = []

  # init q with supplies
  for elem in supplies:
    q.append(elem)

  result = []
  while q:
    node = q.pop(0)
    visited[node] = True
    if node in set(recipes):
      result.append(node) # if node is a recipe, add
    for ns in adj_list[node]:
      in_degree[ns] -=1
      if in_degree[ns] == 0 and visited[ns] == False:
        q.append(ns)
  return result


print(find_recipes(["bread","sandwich","burger"] , [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]] , ["yeast","flour","meat"]))