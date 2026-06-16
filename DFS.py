'''Real-Time Uses of Depth-First Search (DFS) 
DFS dives as deep as possible down a single path before backtracking to try another. It requires less memory than BFS because it doesn't need to store all the nodes at the current level. DFS is the go-to algorithm for exploring every single possibility, checking connectivity, or analyzing dependencies.

===============
Game AI and Decision Trees (e.g., Chess or Mazes)
In a game like Chess, an AI needs to look ahead several moves. DFS is used to simulate a specific sequence of moves all the way to the end of the game (win, lose, or draw) before backtracking to try an alternative opening move.

================
Build Systems & Dependency Resolution (Topological Sort)
When you compile a software project or use a package manager (like npm or pip), certain packages must be installed before others. DFS is used to traverse the dependency graph and determine the exact, correct order of operations (called a Topological Sort).

=====================
Graphics Software (The "Flood Fill" Tool)
When you use the "Paint Bucket" tool in Microsoft Paint, Photoshop, or a digital art app to fill an enclosed area with color, a variant of DFS is often used. It picks a pixel, dives deep into its neighboring pixels of the same color, and changes them until it hits the boundary.

====================
Puzzle Solving & Dead-End Detection
Web crawlers looking to thoroughly map out a specific website's deep directory structure, or algorithms designed to solve a complex maze where you just need any valid exit (not necessarily the shortest one), rely heavily on DFS.

'''

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size  

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
            
    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end=' ')

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_vertex_data):
        visited = [False] * self.size
        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

g.print_graph()

print("\nDepth First Search starting from vertex D:")
g.dfs('D')

#Python
