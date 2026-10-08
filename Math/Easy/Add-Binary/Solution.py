class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=""
        carry=0
        a = a[::-1]
        b = b[::-1]
        for i in range(max(len(a), len(b))):
            digitA=int(a[i]) if i<len(a) else 0
            digitB=int(b[i]) if i<len(b) else 0

            total=digitA+digitB+carry
            ch=str(total%2) # this is binary so for base 2
            res=ch+res #put the new digit at the beginning, then you do not need to rev the res 
            carry=total//2
        
        if carry:
            res="1"+res
        return res