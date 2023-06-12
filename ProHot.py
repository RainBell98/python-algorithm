import heapq

def solution(scoville,K):
    cnt = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)
    while heap[0]<K:
        heapq.heappush(heap,heapq.heappop(heap)+heapq.heappop(heap)*2)
        cnt+=1
        if len(heap)<2 and heap[0]<K:
            return -1
    return cnt