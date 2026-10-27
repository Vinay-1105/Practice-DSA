class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ans=[1]
        for i in range(rowIndex):
            next_row=[0]*(len(ans)+1)
            for j in range(len(ans)):
                next_row[j] += ans[j]
                next_row[j+1] += ans[j]
            ans=next_row
        return ans