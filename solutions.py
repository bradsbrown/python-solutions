# from itertools import permutations

# # question 1
# def question1(s, t):
#     if not s or not t or type(s) is not str or type(t) is not str or len(t) > len(s):
#         return False
#     s = s.lower()
#     t = t.lower()
#     t = [''.join(p) for p in permutations(t)]
#     print t
#     for i in t:
#         if i in s:
#             return True
#     return False

# print question1('udacity', 'aud'), "\n"
# # should return TRUE

# print question1(0,0), "\n"
# # should return FALSE

# print question1(" "," "), "\n"
# # should return TRUE

# print question1("OnBelayClimbOn", "BelayOnClimbing"), "\n"
# # should return FALSE
        
# # question 2
# def isPalindrome(s):
# 	s = s.lower()
# 	return s[::-1] == s

# def question2(s):
# 	if s != None and type(s) is str:

# 		l = ""

# 		for count, item in enumerate(s):
# 			for index, item in enumerate(s):
# 				c = s[count:index + 1]

# 				if isPalindrome(c) and len(c) > len(l):
# 					l = c

# 		return l.lower()
# 	return False


# print question2('racecar'), "\n"
# # Should return 'racecar'

# print question2('SAMMY'), "\n"
# # Should return 'mm'

# print question2(3,3,'hey'), "\n"
# # Should return False



