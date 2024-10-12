# Algorithms

### Binary Search

**binary_search.py**

The time complexity of the find_target function is O(log n), where n is the length of the source_array.

This is because the function uses a binary search algorithm, which divides the search space in half at each step. The while loop continues until the left_index and right_index converge, which happens when the target is found or when the search space is empty.

The key operations in the function are:

Calculating the mid_point using integer division: O(1)
Comparing the source_array[mid_point] with the target: O(1)
Updating the left_index or right_index based on the comparison: O(1)
Since these operations are performed at each step of the binary search, the total time complexity is O(log n), where n is the length of the source_array.

Note that this is an efficient algorithm for finding an element in a sorted array, especially for large arrays. The binary search algorithm reduces the search space by half at each step, making it much faster than a linear search algorithm, which would have a time complexity of O(n).


### Valid Anagram

**anagram.py**

The time complexity of the is_anagram function is O(n), where n is the length of the input strings s and t.

Here's a breakdown of the operations performed in the function:

Length comparison: The function first checks if the lengths of s and t are equal, which takes O(1) time.
Dictionary creation: The function creates two dictionaries, s_dict and t_dict, to store the character frequencies of s and t, respectively. This takes O(n) time, as each character in the strings is processed once.
Dictionary iteration: The function then iterates over the keys of s_dict and checks if each key is present in t_dict with the same frequency. This takes O(n) time, as each key in s_dict is processed once.
Return statement: The function returns a boolean value indicating whether s and t are anagrams, which takes O(1) time.
Since the dictionary creation and iteration steps dominate the time complexity, the overall time complexity of the is_anagram function is O(n).

Note that this is an efficient algorithm for checking if two strings are anagrams, especially for large strings. The use of dictionaries allows for fast lookups and frequency counting, making the algorithm much faster than a naive approach that compares characters one by one.


### 1768. Merge Strings Alternately

**merge_strings_alternately.py**

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

 

Constraints:

    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.



### 1071. Greatest Common Divisor of Strings

**gcd_string.py**


For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

 

Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.

