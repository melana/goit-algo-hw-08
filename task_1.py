import heapq 

def connect_cables(cables: list):

    heapq.heapify(cables) # перетворюємо list з вхідними даними на heap
    res = 0 # загальні витрати

    while len(cables) !=1:
        min1 = heapq.heappop(cables) # дістаємо 2 найкоротші кабелі
        min2 = heapq.heappop(cables)
        connected = min1 + min2 # з'єднуємо їх
        res = res + connected # додаємо їх суму до загальних витрат
        heapq.heappush(cables, connected) # повертаємо їх суму назад у кучу

    return res

# Test
cables_list = [6, 3, 4, 1]
total = connect_cables(cables_list)
print (total) # 26
