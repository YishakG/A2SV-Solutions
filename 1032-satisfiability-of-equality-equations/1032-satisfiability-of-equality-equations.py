class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        def find(x):
            if x != parent.setdefault(x, x):
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)
        for eq in equations:
            if eq[1:3] == "==":
                union(eq[0], eq[3])
        for eq in equations:
            if eq[1:3] == "!=":
                if find(eq[0]) == find(eq[3]):
                    return False

        return True