class Solution:
    def removeStars(self, s: str) -> str:
        star=[]
        for x in s:
            if x!="*":
                star.append(x)
            else:
                star.pop()
        return "".join(star)