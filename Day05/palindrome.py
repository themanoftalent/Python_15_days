#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

# function which return reverse of a string
def reverse(s):
	return s[::-1]

def isPalindrome(s):
	# Calling reverse function
	rev = reverse(s)

	# Checking if both string are equal or not
	if (s == rev):
		return True
	return False


# Driver code
s=input('Enter your word = ')

ans = isPalindrome(s)

if ans == 1:
	print("Yes")
else:
	print("No")

