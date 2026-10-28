class Solution:
    def countPrimes(self, n: int) -> int:
        # res=0
        # if n==0 or n==1:
        #     return 0
        
        # for p in range(2,n):
        #     for div in range(2,p):
        #         if p%div==0:
        #             break
        #         else:
        #             res+=1
        # return res
        if n<=2:
            return 0
        prime=[True]*n
        prime[0]=prime[1]=False
        for p in range(2,int(n**0.5)+1):
            if prime[p]:
                prime[p*p:n:p]=[False]*((n-1-p*p)//p+1)
        return sum(prime)