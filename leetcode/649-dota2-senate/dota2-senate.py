from collections import deque

class Solution:
    def available(self, dq, rq):
        return len(dq) > 0 and len(rq) > 0

    def announce(self, dq, rq):
        if len(dq) > 0:
            return "Dire"
        return "Radiant"

    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        dq, rq = deque(), deque()

        for i, s in enumerate(senate):
            if s == "R":
                rq.append(i)
            else:
                dq.append(i)

        while self.available(dq, rq):
            d, r = dq.popleft(), rq.popleft()
            if d < r:
                dq.append(d + n)
            else:
                rq.append(r + n)
        
        return self.announce(dq, rq)



        