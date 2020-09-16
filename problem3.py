class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {}
        
        for e in employees:
            d[e.id] = e
        
        queue = [id]
        score = 0
        while queue:
            current = queue.pop(0)
            score += d[current].importance
            queue = queue + d[current].subordinates
        return score