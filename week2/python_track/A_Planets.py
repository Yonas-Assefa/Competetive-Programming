no_test = int(input())
ans = []
 
for i in range(no_test):
    planet_cost = list(map(int,input().split(" ")))
    planets = list(map(int,input().split(" ")))
 
    machine_cost = planet_cost[1]
    orbital_plantets = {}
 
    for plt in planets:
        orbital_plantets[plt] = orbital_plantets.get(plt, 0) + 1
 
    total_cost = 0
    for orb in orbital_plantets:
        cost = min(orbital_plantets[orb], machine_cost)
        total_cost += cost
    
    ans.append(total_cost)
 
for i in ans:
    print(i)