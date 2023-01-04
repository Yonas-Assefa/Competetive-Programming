class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        match_stat = defaultdict(lambda:[0,0])

        for match in matches:
            match_stat[match[0]][0] += 1
            match_stat[match[1]][1] += 1
        
        win_all = []
        lost_one = []

        for stat in match_stat:
            if match_stat[stat][1] == 0:
                win_all.append(stat)
                
            if match_stat[stat][1] == 1:
                lost_one.append(stat)
        
        win_all.sort()
        lost_one.sort()

        return [win_all, lost_one]
        