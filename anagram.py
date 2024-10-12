# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def is_anagram(s, t):

    if len(s) != len(t):
        return False

    s_dict = {}
    t_dict = {}

    for i in range(len(s)):
        s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        t_dict[t[i]] = t_dict.get(t[i], 0) + 1

    for key in s_dict:
        if key not in t_dict or s_dict[key] != t_dict[key]:
            return False

    return True


s = "anagram"
t = "nagaram"
print(is_anagram(s, t))