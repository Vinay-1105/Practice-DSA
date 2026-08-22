class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=str(n)
        sum=0
        product=1
        for ch in s:
            digit=int(ch)
            sum+=digit
            product*=digit
        return n%(sum + product) == 0