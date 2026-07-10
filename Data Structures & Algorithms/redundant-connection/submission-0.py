from copy import copy

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        
        visited = set()
        graph = defaultdict(list)
        for [a, b] in edges:
            graph[a].append(b)
            graph[b].append(a)

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

        dfs(edges[0][0], -1)
        f_visited = frozenset(visited)

        result = []
        for j in range(len(edges)):
            visited = set()
            edg = copy(edges)
            edg.pop(j)
            graph = defaultdict(list)
            for [a, b] in edg:
                graph[a].append(b)
                graph[b].append(a)

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
            dfs(edg[0][0], -1)
            if visited:
                result.append((j, frozenset(visited)))
        out = None
        for (j, r) in result:
            if r == f_visited:
                out = edges[j]
        return out
