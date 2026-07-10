class Solution:
    from collections import defaultdict
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        m_edges = defaultdict(list)
        for [a, b] in edges:
            m_edges[a].append(b)
            m_edges[b].append(a)

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for s in m_edges[node]:
                if s == parent:
                    continue
                elif s in visited:
                    return False
                elif not dfs(s, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n

        