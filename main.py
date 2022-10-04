cities = [ ["New York", "London"],
              ["Parij", "Madrid"],
              ["Madrid", "Dubai"],
              ["Berlin", "Parij"],
              ["Praga", "Berlin"],
              ["London", "Praga"]]

def find_last_city(cities):
    last = cities[0][1]
    for city in cities:
        if city [1] not in [i[0] for i in cities]:
            last = city[1]
            break
    print(last)
find_last_city(cities)
