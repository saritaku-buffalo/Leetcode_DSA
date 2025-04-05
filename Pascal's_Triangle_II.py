
# dynamic programming (bottom-up)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            row_next = [0] * (len(res) + 1 )
            for j in range(len(res)):
                row_next[j] += res[j]
                row_next[j + 1] += res[j]
            res = row_next
        return res
        
        