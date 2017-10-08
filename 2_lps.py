
# question 2
def isPalindrome(s):
	s = s.lower()
	return s[::-1] == s

def question2(s):
	if s != None and type(s) is str:

		l = ""

		for count, item in enumerate(s):
			for index, item in enumerate(s):
				c = s[count:index + 1]

				if isPalindrome(c) and len(c) > len(l):
					l = c

		return l.lower()
	return -1


print question2('racecar'), "\n"
# returns 'racecar'

print question2('SAMMY'), "\n"
# returns 'mm'

print question2(None), "\n"
# returns -1




