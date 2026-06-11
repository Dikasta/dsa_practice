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
