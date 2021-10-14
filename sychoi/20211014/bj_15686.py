def distance(h, c):
    x1, y1 = h
    x2, y2 = c
    
    return abs(x1-x2) + abs(y1-y2)

def find_idx(n, city):
    idxs = []
    for i in range(len(city)):
        for j in range(len(city[i])):
            if city[i][j] == n:
                idxs.append((i, j))
                
    return idxs

def sum_distance(chicken, houses):
    dist = 0
    for house in houses:
        dist += distance(house, chicken)
    return dist

def min_distance(chickens, house):
    min_value = 987654321

    for chicken in chickens:
        if min_value > distance(house, chicken):
            min_value = distance(house, chicken)
    return min_value

if __name__=='__main__':
    n, m = map(int, input().split())
    city = []
    for i in range(n):
        city.append(list(map(int, input().split())))

    houses = find_idx(1, city)
    chickens = find_idx(2, city)

    chicken_dict = {}
    for chicken in chickens:
        chicken_dict[chicken] = sum_distance(chicken, houses)
    sorted_dict = sorted(chicken_dict.items(), key = lambda item: item[1])
    sorted_dict = [x[0] for x in sorted_dict]

    chickens_ = sorted_dict[:m]
    answer = 0
    for house in houses:
        answer += min_distance(chickens_, house)
    print(answer)
