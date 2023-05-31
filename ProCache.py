def solution(cacheSize,cities):
    cache = []
    answer = 0
    for city in cities:
        city = city.upper()
        if not city in cache:
            if len(cache)<cacheSize:
                cache.append(city)

            else:
                cache.append(city)
                cache.pop(0)
            answer +=5
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer +=1
    return answer
print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))