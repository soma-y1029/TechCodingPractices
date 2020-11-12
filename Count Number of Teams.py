class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # backtrack 
        # pick fist rating that satisfy the condition 
        
        count = 0
        def backtrack(i=0, team=[]):
            nonlocal count
            # print(f'{i=} {team=}')
            # base case  
            if len(team) >= 3:
                # check condition 
                if team[0] < team[1] < team[2] or team[0] > team[1] > team[2]:
                    return team
                return
            if i >= len(rating):
                return
            
            
            # recursive case
            for j, rate in enumerate(rating[i:]):
                formed_team = backtrack(i+j, team+[rate])
                if formed_team is not None:
                    count += 1
                
        backtrack()
        return count
                
            
