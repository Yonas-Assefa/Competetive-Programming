class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_skill = sum(skill)
        no_teams = len(skill) / 2
        team_skill = total_skill / no_teams
        chemistry = 0

        skill.sort()
        left = 0
        right = len(skill) - 1
        while left < right:
            if skill[left] + skill[right] == team_skill:
                prod = skill[left] * skill[right]
                chemistry += prod
                right -= 1
                left += 1
            else:
                return -1
            
        return chemistry