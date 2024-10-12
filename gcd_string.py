

import math
def gcdOfStrings(str1: str, str2: str) -> str:
        len_1, len_2 = len(str1), len(str2)

        gcd = math.gcd(len_1, len_2)

        list_1, list_2 = list(str1), list(str2)

        prefix_1 = "".join(list_1[:gcd])
        prefix_2 = "".join(list_2[:gcd])

        if prefix_1 == prefix_2:
            multiple_1 = len_1 // gcd
            if str1 == prefix_1 * multiple_1:
                multiple_2 = len_2 // gcd
                if str2 == prefix_1 * multiple_2:
                    return prefix_1
                else:
                    return ""
            else:
                return ""

        else:
            return ""
        

str1 = "abcabc"
str2 = "abc"
print(gcdOfStrings(str1, str2))