from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n
        graph = defaultdict(list)
        for [a, b] in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        result = []
        for j in range(n):
            visited = set()

            def dfs(node, parent):
                visited.add(node)
                for i in graph[node]:
                    if i == parent:
                        continue
                    elif i in visited:
                        continue
                    else:
                        dfs(i, node)
                return True
            dfs(j, -1)
            if visited:
                result.append(visited)

        return len({frozenset(s) for s in result})
        
        
            

        

