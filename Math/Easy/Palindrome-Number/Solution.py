class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str1 = str(x)
        str2 = str1[::-1]
        if str1==str2:
            return True
        return False