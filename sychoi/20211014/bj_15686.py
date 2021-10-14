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

if __name__=='__main__':
    n, m = map(int, input().split())
    city = []
    for i in range(n):
        city.append(list(map(int, input().split())))

    houses = find_idx(1, city)
    chickens_idx = find_idx(2, city)

    from itertools import combinations
    chickens_ = list(combinations(chickens_idx, m))
    answer = 9876543
    for chickens in chickens_:
        temp = 0
        for house in houses:
            min_v = 8765432
            for chicken in chickens:
                if min_v > distance(house, chicken):
                    min_v = distance(house, chicken)
            temp += min_v

        if answer > temp:
            answer = temp


    print(answer)
