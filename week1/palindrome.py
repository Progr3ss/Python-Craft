
"""
Recipe for designing functions
1.examples
2.type contract
3.header
4.descrption
5.body
6.test

(str) -> Bool
Return True if and only if s is a palindrome. 


is_palindrome("noon")
return True
is_palindrome("dented")
return False
"""

def is_palindrome_v1(s):

  #(str) -> Bool
  #Return True if and only if s is a palindrome. 
    
    return s == reverseString(s)


def is_palindrome_v2(s):
    """
    (str) -> bool 
    Return True iff s is a palindrome

    is_palindrome_v2("noon")
    True

    """
    n = len(s)
    return s[:n//2] == reverseString(s[n-n//2:])

def is_palindrome_v3(s):
    """
    (str) -> bool 
    Return True iff s is a palindrome
    """
    i = 0 
    j = len(s) - 1

    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1

    return j <= i 


def reverseString(s):

#(str) -> str
#reverse("hello")
#Return a reversed version of s.
#"olleh"
    rev = ''
    for ch in s:
       rev = ch + rev

    return rev
print(is_palindrome_v3("racecar"))
print(is_palindrome_v2("racecar"))
print(is_palindrome_v1("racecar"))
