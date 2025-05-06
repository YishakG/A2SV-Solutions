class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(email):
            if parent[email] != email:
                parent[email] = find(parent[email])
            return parent[email]

        def union(email1, email2):
            root1 = find(email1)
            root2 = find(email2)
            if root1 != root2:
                parent[root2] = root1

        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                union(first_email, email)
                email_to_name[email] = name
        roots = defaultdict(list)
        for email in parent:
            root = find(email)
            roots[root].append(email)

        # Step 3: Format the result
        merged = []
        for root_email, emails in roots.items():
            merged.append([email_to_name[root_email]] + sorted(emails))

        return merged