https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3555/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            #nt(f'{i=}, {n=}, {flowerbed=}')
            if flowerbed[i]:
                i += 2
                
            elif not flowerbed[i]:
                left = flowerbed[i-1] if i > 0 else flowerbed[0]
                right = flowerbed[i+1] if i < len(flowerbed)-1 else 0
                #print(left, right)
                if not left and not right:
                    flowerbed[i] = 1
                    n -= 1
                    i += 2 
                else:
                    i += 1
            
            if n <= 0:
                return True
            
        return False
