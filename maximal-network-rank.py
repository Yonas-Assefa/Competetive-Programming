class Solution:
		def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
			if roads == []: #egde case check
				return 0

			#create adjacency matrix  to check if edge present or not in O(1) time
			adj=[[0]*(n) for i in range(n)]
			for i in roads:
				adj[i[0]][i[1]] = 1
				adj[i[1]][i[0]] = 1

			node_degrees = defaultdict(int)
			for i in roads:
				node_degrees[i[0]]+=1
				node_degrees[i[1]]+=1

			maxx1, maxx2 = 0, 0
			ans = 0
			for i, k in node_degrees.items():                #O(N)
				if k >= maxx1:
					maxx1 = k
					maxx2 = 0
					for j, l in node_degrees.items():                #O(N)
						if l >= maxx2 and j!=i:
							maxx2 = l
							if adj[i][j] == 1 or adj[j][i] == 1:                #O(1)
								ans = max(ans, maxx1 + maxx2 - 1)
							else:
								ans = max(ans, maxx1 + maxx2 )
			return ans