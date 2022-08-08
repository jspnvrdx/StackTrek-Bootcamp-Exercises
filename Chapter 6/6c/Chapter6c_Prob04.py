import os
os.system('cls||clear')

#----CODE STARTS HERE------

def isPalindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return isPalindrome(s[1:-1])
        else:
            return False

def display(s):
    if(isPalindrome(s)==True):
        return "That was a palindrome"
    else:
        return "That is not a palindrome"
