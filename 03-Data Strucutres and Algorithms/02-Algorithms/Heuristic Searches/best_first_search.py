"""
Best-First-Search Heurisitic on
NxN search space (matrix).

Matrix:
    - 0's are free cells.
    - 1's are walls.

In this technique we evaluate all
neighbors based on their manhattan
distance to the goal and add them
to the Priority Queue.

Everytime we pop a item from the
PQ it will be the closest item to
the goal.

If there is no path from source to 
target the loop will end and inform
the user that no path was found.
"""

import sys
import heapq

__author__ = "Rafael Broseghini"

class Item(object):
    def __init__(self, coord, distance):
        self.coord = coord
        self.distance = distance

    @property
    def distance(self):
        return self._distance
    
    @distance.setter
    def distance(self, nv):
        self._distance = nv

    @property
    def coord(self):
        return self._coord

    @coord.setter
    def coord(self, nv):
        self._coord = nv
  
    def __lt__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Can only compare to Item class")
        return self.distance < other.distance

    def __gt__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Can only compare to Item class")      
        return self.distance > other.distance

def mhd(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def get_neighbors(graph: list, coord: list):
    neighbors = []
    append_neighbors(coord[0]-1, coord[1], graph, neighbors)
    append_neighbors(coord[0]+1, coord[1], graph, neighbors)
    append_neighbors(coord[0], coord[1]-1, graph, neighbors)
    append_neighbors(coord[0], coord[1]+1, graph, neighbors)
    
    return neighbors

def append_neighbors(x: int, y: int, graph: list, array:list):
    if x >= 0 and x <= len(graph)-1 and y >= 0 and y <= len(graph[0])-1:
        if graph[x][y] != 1 and graph[x][y] != "1":
            array.append([x, y])

def best_first_search(graph, source, goal):
    visited, unvisited, path = [tuple(source)], [], []
    heapq.heappush(unvisited,Item(source, 0))

    while len(unvisited) > 0:
        curr = heapq.heappop(unvisited)
        path.append(curr.coord)
        if curr.coord == goal:
            return path

        neighbors = get_neighbors(graph, curr.coord)
        for n in neighbors:
            if tuple(n) not in visited:
                visited.append(tuple(n))
                dis = mhd(n, goal)
                heapq.heappush(unvisited, Item(n, dis))

    return []

def draw_path(x: int, y: int, source: list, goal: list, path: list, space: list):
    drawing = [["O" if space[j][i] == 0 else "|" for i in range(x)] for j in range(y)]
    x_source, y_source = source[0], source[1]
    x_goal, y_goal = goal[0], goal[1]
    step = 0
    for coord in path:
        x, y = coord[0], coord[1]
        # drawing[x][y] = f"{step}"
        # or
        drawing[x][y] = "X"
        if space[x][y] != 1:
            step += 1
    drawing[x_source][y_source] = "S"
    drawing[x_goal][y_goal] = "T"

    for line in drawing:
        print(" ".join(line))

def read_search_space(filename: str):
    search_space = []
    with open(filename, "r") as infile:
        for line in infile:
            search_space.append(list(map(int, line.split())))

    return search_space

def main():
    space = read_search_space("search_spaces_data/space2.txt")
    source, target = [0,0], [0, 9]
    path = best_first_search(space, source, target)
    if len(path) > 0:
        for line in space:
            print(" ".join(str(x) for x in line))
        print() 
        draw_path(len(space[0]), len(space), source, target, path, space)


if __name__ == "__main__":
    main()


