"""Given a string, return the length of the longest palindromic substring in it.
A string is a palindrome when it reads the same backward as forward.
Write a function longestPalindromicSubstringLength(s: str) -> int to determine the length of the longest palindromic substring in the given
string.
Example 1: Input: s ="babad"
Output: 3
Explanation: The longest palindromic substring is "bab" or "aba".
 
Example 2: Input: s ="cbbd"
Output: 2
Explanation: The longest palindromic substring is "bb".
 
Constraints:
• 1 =< s.length =< 1000
• s consists of lowercase English letters."""

def longestPalindromicSubstringLength(s: str) -> int:
    def expand_palindrome(i, j): # cbbd
        count = 0
        size = len(s)
        while j > -1 and i < size and s[i] == s[j]:
            count += 1 
            i += 1
            j -= 1
        return count 
   
    # aba,  abba
    if not s:
        return 0
    elif len(s) == 1:
        return 1 
    resultado = 0

    for i in range(1, len(s)):
        tamaño = max(expand_palindrome(i, i), expand_palindrome(i -1, i))
        if tamaño > resultado:
            resultado = tamaño
    return resultado

print(longestPalindromicSubstringLength("cbbd"))   
print(longestPalindromicSubstringLength("bab"))   