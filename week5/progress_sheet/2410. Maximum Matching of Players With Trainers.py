class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        top = 0
        botm = 0
        len1 = len(players)
        len2 = len(trainers)
        res = 0
        while top < len1 and botm < len2:
            if players[top] <= trainers[botm]:
                top += 1
                botm += 1
                res += 1
            else:
                botm += 1
        return res

        