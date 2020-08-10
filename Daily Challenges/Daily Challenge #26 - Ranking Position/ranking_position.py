def points(e):
  return e['points']

def name(e):
  return e['name']

def position_ranking():
    contestants = [
  {
    'name': "John",
    'points': 100,
  },
  {
    'name': "Bob",
    'points': 130,
  },
  {
    'name': "Mary",
    'points': 120,
  },
  {
    'name': "Kate",
    'points': 120,
  }
]
    contestants.sort(key=name)
    contestants.sort(key=points, reverse=True)
    cont = 0
    while cont < len(contestants):
        if contestants[cont] == contestants[-1]:
            contestants[cont]["position"] = cont+1
            cont += 1
        elif contestants[cont]["points"] == contestants[cont+1]["points"]:
            contestants[cont]["position"] = cont+1
            contestants[cont+1]["position"] = cont+1
            cont += 2
        else:
            contestants[cont]["position"] = cont+1
            cont += 1

    return contestants

if __name__ == "__main__":
    print(position_ranking())