https://leetcode.com/contest/weekly-contest-218/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        parser = {'G':'G', '()': 'o', '(al)':'al'}
        letter, res = '', ''
        for x in command:
            letter += x
            # print(f'{x=}, {letter=}')
            if parser.get(letter):
                res += parser.get(letter)
                letter = ''
                
        return res
