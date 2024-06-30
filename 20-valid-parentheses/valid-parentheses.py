class Solution:
    def isValid(self, s: str) -> bool:
        res=[]
        if(s[0]==")" or s[0]=="}" or s[0]=="]"):
            return False
        for i in s:
            if(i=="(" or i=="{" or i=="["):
                res.append(i)
            elif(len(res)!=0 and (res[-1]=="(" or res[-1]=="{" or res[-1]=="[")):
                if((i==")" and res[-1]=="(") or (i=="}" and res[-1]=="{") or (i=="]" and res[-1]=="[")):
                    res.pop()
                else:
                    return False
            else:
                return False
        
        if(len(res)==0):
            return True
        return False
