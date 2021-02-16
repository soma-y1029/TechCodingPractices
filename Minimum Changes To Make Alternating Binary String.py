https://leetcode.com/contest/weekly-contest-228/problems/minimum-changes-to-make-alternating-binary-string/


class Solution:
    def minOperations(self, s: str) -> int:
        res = float('inf')
        for first in ['0', '1']:
            st = list(s)
            tmp = 0
            if st[0] != first: tmp += 1;
            st[0] = first
            # print('start', tmp, st)
            for i, b in enumerate(st[1:], 1): 
                if st[i-1] == b: 
                    print(i, st[i-1], b)
                    st[i] = '0' if b == '1' else '1'
                    tmp += 1
                    # print('changed', tmp, st)
            # print('end', tmp, st)
            res = min(res, tmp)
        
        return res
