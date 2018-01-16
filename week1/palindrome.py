
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

def reverseString(s):

#(str) -> str
#reverse("hello")
#Return a reversed version of s.
#"olleh"
    rev = ''
    for ch in s:
       rev = ch + rev

    return rev


print(is_palindrome_v1("racecar"))
