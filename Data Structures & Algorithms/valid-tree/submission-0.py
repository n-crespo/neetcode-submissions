class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        if not n:
            return True

        for i in range(n):
            adj[i] = []
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False # detected a loop!

            visit.add(i)

            # check all neighbors
            for j in adj[i]:
                # we allow an edge from a node to itself
                if j == prev:
                    continue

                # check if each neighbor is valid
                validTree = dfs(j, i)
                if not validTree:
                    return False
            return True

        return dfs(0, -1) and n == len(visit)




        