import heapq

pq = []
heapq.heappush(pq, 456)
heapq.heappush(pq, 123)
heapq.heappush(pq, 789)
print("size: ",len(pq))
while len(pq)>0:
    print(heapq.heappop(pq))