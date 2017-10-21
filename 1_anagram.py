'''
Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.
'''



def question1(s, t):
    if (s and t) and (type(s) is not int and type(t) is not int):
        for letter in t:
            # check if letter exists in string
            if not letter in s:
                return False
            # check num of occurances for letter
            count = t.count(letter)
            if count > 1:
                count_2 = s.count(letter)
                # check that num of occurances match
                if count > count_2:
                    return False  
        return True
    return -1

print question1('udacity', 'aud'), "\n"
# returns TRUE

print question1(0,0), "\n"
# returns -1

print question1(" "," "), "\n"
# returns TRUE

print question1("OnBelayClimbOn", "BelayOnClimbing"), "\n"
# returns FALSE




