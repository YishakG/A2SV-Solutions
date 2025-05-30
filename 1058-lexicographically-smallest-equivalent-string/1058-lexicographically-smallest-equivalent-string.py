class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for a, b in zip(s1, s2):
            pa, pb = find(ord(a) - ord('a')), find(ord(b) - ord('a'))
            if pa < pb:
                parent[pb] = pa
            else:
                parent[pa] = pb

        result = []
        for c in baseStr:
            smallest_char = chr(find(ord(c) - ord('a')) + ord('a'))
            result.append(smallest_char)
        return ''.join(result)