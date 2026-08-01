class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        li=s.split()
        return " ".join(li[::-1])
        