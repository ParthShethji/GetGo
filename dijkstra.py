import sys


class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSolution(self, dist):
		print("Vertex \t Distance from Source")
		temp=[]
		for node in range(self.V):
			# print(node, "\t\t", dist[node], "\n")
			temp.append(dist[node])
		print(temp)

	def minDistance(self, dist, sptSet):

		min = 1e7


		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index


	def dijkstra(self, src):

		dist = [1e7] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			
			u = self.minDistance(dist, sptSet)

			
			sptSet[u] = True

	
			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]

		self.printSolution(dist)

# Driver program
g = Graph(10)
g.graph = [[0, 0, 0, 0, 20, 10, 0, 0, 0, 0],
		[0, 0, 33.541, 0, 0, 28.2, 0, 18.02, 0, 36.4],
		[0, 33.541, 0, 0, 0, 0, 25, 29.561, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 39.05, 0, 32],
		[20, 0, 0, 0, 0, 20, 0, 0, 0, 0],
		[10, 0, 0, 0, 20, 0, 31.6, 0, 0, 0],
		[0, 0, 25, 0, 0, 31.6, 0, 0, 0, 0],
		[0, 18.02, 29.561, 39.05, 0, 0, 0, 0, 20.61, 0],
		[0, 0, 0, 0, 0, 0, 20.61, 0, 0, 0],
		[0, 36.4, 0, 32, 0, 0, 0, 0, 0, 0],
	
    ]

if sys.argv[1] == "katraj":
	g.dijkstra(1)
elif sys.argv[1] == "swargate":
	g.dijkstra(2)




