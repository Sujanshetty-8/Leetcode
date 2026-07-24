class Solution:
    def reverseVowels(self, s: str) -> str:
        i,j=0,len(s)-1
        vowels=set('aeiouAEIOU')
        ch=list(s)
        while i<j:
            while i<j and ch[i] not in vowels:
                i+=1
            while i<j and ch[j] not in vowels:
                j-=1
            ch[i],ch[j]=ch[j],ch[i]
            i+=1
            j-=1
        return "".join(ch)