https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for num in range(1, n+1):
            if not num%5 and not num%3:
                res.append('FizzBuzz')
            elif not num%5:
                res.append('Buzz')
            elif not num%3:
                res.append('Fizz')
            else:
                res.append(str(num))
        return res
