# 953. Verifying an Alien Dictionary

# Easy

# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
# 
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
# 
#  
# 
# Example 1:
# 
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:
# 
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:
# 
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
#  
# 
# Constraints:
# 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.
# 
#

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = { char:i for i,char in enumerate(order)}
        n = len(words)
        for i in range(1,n):
            if not self.isLexi(words[i-1], words[i],d):
                return False
        return True
    def isLexi(self, word1,word2,d):
        n,m=len(word1),len(word2)
        for i in range(min(n,m)):
            if d[word1[i]] > d[word2[i]]:
                return False
            elif d[word1[i]] == d[word2[i]]:
                continue
            else:
                return True

        return True if n<=m else False

# The words of A are the finite sequences of symbols from A, including words of length 1 containing a single symbol, words of length 2 with 2 symbols, and so on, even including the empty sequence {\displaystyle \varepsilon }\varepsilon  with no symbols at all. The lexicographical order on the set of all these finite words orders the words as follows:
# 
# Given two different words of the same length, say a = a1a2...ak and b = b1b2...bk, the order of the two words depends on the alphabetic order of the symbols in the first place i where the two words differ (counting from the beginning of the words): a < b if and only if ai < bi in the underlying order of the alphabet A.
# If two words have different lengths, the usual lexicographical order pads the shorter one with "blanks" (a special symbol that is treated as smaller than every element of A) at the end until the words are the same length, and then the words are compared as in the previous case.
#


