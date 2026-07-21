class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Sort the list lexicographically
        strs.sort()
        
        # First string in sorted list
        first = strs[0]
        
        # Last string in sorted list
        last = strs[-1]
        
        # Store the common prefix characters
        ans = []
        
        # Compare characters of first and last string
        for i in range(min(len(first), len(last))):
            # Stop if characters differ
            if first[i] != last[i]:
                return ''.join(ans)
            # Add matching character to result
            ans.append(first[i])
        
        # Return the longest common prefix
        return ''.join(ans)       

        