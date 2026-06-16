'''Option A: Breadth-First Search (BFS) — Best for Unweighted Mazes
If every step the mouse takes costs the exact same amount of energy, BFS is the perfect choice.

How it works: The mouse explores the maze layer by layer, expanding equally in all directions (up, down, left, right) from its starting point.'''
#=============================
'''
GPS & Map Navigation (e.g., Google Maps)
When you ask for the fewest number of turns, or the shortest distance on a subway map, BFS is running under the hood. It checks all immediate neighboring intersections first, guaranteeing that the first time it hits your destination, it has found the shortest route.

=========

Social Network Connections (e.g., LinkedIn & Facebook)
LinkedIn: When you see a profile marked as a "2nd-degree connection," BFS calculated that. It looks at your immediate friends (1st degree), then their friends (2nd degree), and so on.

Facebook: Features like "People You May Know" rely on BFS to find mutual friends within a close radius of your profile.

===================
Network Broadcasting & Peer-to-Peer (P2P) Networks
In torrent software (like BitTorrent) or routing protocols, when a node needs to find a file or broadcast a message to the entire network efficiently, it uses BFS (specifically, a method called Flooding) to send the packet to all nearest neighbors first.
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

    def bfs(self, start_vertex_data):
        queue = [self.vertex_data.index(start_vertex_data)]
        visited = [False] * self.size
        visited[queue[0]] = True

        while queue:
            current_vertex = queue.pop(0)
            print(self.vertex_data[current_vertex], end=' ')

            for i in range(self.size):
                if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True


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

print("\nBreadth First Search starting from vertex D:")
g.bfs('D')

# Python
