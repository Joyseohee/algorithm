class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        str_arr = list(s)

        start, end = 0, n - 1

        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        while start < end:
            if str_arr[start] in vowels and str_arr[end] in vowels:
                str_arr[start], str_arr[end] = str_arr[end], str_arr[start]
                start += 1
                end -= 1

            elif str_arr[start] in vowels and str_arr[end] not in vowels:
                end -= 1

            elif str_arr[start] not in vowels and str_arr[end] in vowels:
                start += 1

            else:
                start += 1
                end -= 1
                

        return "".join(str_arr)