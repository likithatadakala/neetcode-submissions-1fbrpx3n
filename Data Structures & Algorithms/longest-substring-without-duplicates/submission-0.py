class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        longest = 0
        
        for right in range(len(s)):
            # If the character is already in our window, shrink from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the new character and update the longest length
            char_set.add(s[right])
            longest = max(longest, right - left + 1)
        
        return longest