from collections import deque
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, 
    k: int) -> int:
        dests = defaultdict(list)
        for [s, d, p] in flights:
            dests[s].append([d, p])

        prices = [float("inf")] * n
        prices[src] = 0

        queue = deque([(src, 0, 0)])  # (node, cost, stops)
        while queue:
            node, cost, stops = queue.popleft()

            if stops > k:
                continue

            for nei, price in dests[node]:
                new_cost = cost + price

                if new_cost < prices[nei]:
                    prices[nei] = new_cost
                    queue.append((nei, new_cost, stops + 1))

        print(prices)

        return prices[dst] if prices[dst] != float("inf") else -1

