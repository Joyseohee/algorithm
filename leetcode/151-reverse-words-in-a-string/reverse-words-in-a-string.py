class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)  # 문자열을 "주어진 문자 배열"이라고 가정하는 셈

        # 위에서 만든 로직 재사용
        self.reverse_words_in_place(chars)

        return "".join(chars)

    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    def reverse_words_in_place(self, chars):
        n = len(chars)
        write = 0
        read = 0

        # leading spaces 제거
        while read < n and chars[read] == ' ':
            read += 1

        # 중복 공백 압축 + trailing space 처리용
        while read < n:
            if chars[read] != ' ':
                chars[write] = chars[read]
                write += 1
            else:
                if write > 0 and chars[write - 1] != ' ':
                    chars[write] = ' '
                    write += 1
            read += 1

        if write > 0 and chars[write - 1] == ' ':
            write -= 1

        del chars[write:]

        # 전체 뒤집기
        self.reverse(chars, 0, len(chars) - 1)

        # 각 단어 뒤집기
        start = 0
        n = len(chars)
        for i in range(n + 1):
            if i == n or chars[i] == ' ':
                self.reverse(chars, start, i - 1)
                start = i + 1
