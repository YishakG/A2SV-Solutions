class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        indexed_tasks.sort()
        result = []
        time = 0
        i = 0
        n = len(tasks)
        min_heap = []

        while i < n or min_heap:
            while i < n and indexed_tasks[i][0] <= time:
                et, pt, idx = indexed_tasks[i]
                heappush(min_heap, (pt, idx))
                i += 1
            
            if min_heap:
                pt, idx = heappop(min_heap)
                time += pt
                result.append(idx)
            else:
                time = indexed_tasks[i][0]

        return result
        