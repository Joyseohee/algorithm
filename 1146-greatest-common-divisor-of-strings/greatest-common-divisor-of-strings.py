class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = 0
        x = ""
        mini = min(len(str1), len(str2))
        c = 1


        # 최대공약수
        for k in range(mini, 1, -1):
            if len(str1) % k == 0 and len(str2) % k == 0:
                c = k
                break


        # 겹치는 부분 찾기
        while i < c:
            if str1[i] == str2[i]:
                x += str1[i]
            else:
                break
            i+=1

        if x == "":
            return ""

        for n in range(i, len(str1), len(x)) :
            if str1[n:n+len(x)] != x:
                x = ""
                break

        if x == "":
            return ""

        for n in range(i, len(str2), len(x)) :
            if str2[n:n+len(x)] != x:
                x = ""
                break

        if x == "":
            return ""

        return x





