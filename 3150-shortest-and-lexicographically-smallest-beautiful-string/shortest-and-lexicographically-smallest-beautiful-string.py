class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n=len(s)
        if n<k:
            return ""
        l=r=0
        res=[]
        count=0
        length=n
        while r<n:
            if s[r]=="1":
                count+=1
            while count==k:
                if r-l+1<=length:
                    if r-l+1<length:
                        res=[]
                        length=r-l+1
                    res.append(s[l:r+1])
                if s[l]=="1":
                    count-=1
                l+=1
            r+=1
        if not res:
            return ""
        res.sort()
        return res[0]