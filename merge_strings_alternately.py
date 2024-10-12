# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

def mergeAlternately( word1: str, word2: str) -> str:
    wl1 = list(word1)
    wl2 = list(word2)
    merged = ""

    length_index = len(wl1)
    if len(wl2) > len(wl1):
        length_index = len(wl2)

    for i in range(length_index):
        if (len(wl1) - 1) >= i:
            merged += wl1[i]
        if (len(wl2) - 1) >= i:
            merged += wl2[i]

    return merged


word1 = "ab"
word2 = "pqrs"
print(mergeAlternately(word1, word2))