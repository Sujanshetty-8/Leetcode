class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        li=list(s)
        vowels=['a','e','i','o','u','A','E','I','O','U']
        i=0
        j=len(li)-1
        while i<j:
            if li[i] in vowels and li[j] in vowels:
                li[i],li[j]=li[j],li[i]
                i+=1
                j-=1
            elif li[i] in vowels:
                j-=1
            else:
                i+=1
        s="".join(li)
        return s
        