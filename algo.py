import math, random
import snake as sk
from queue import PriorityQueue

class Node():
    def __init__(self, parent=None, position=None) -> None:
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

class snakeai():
    def __init__(self, grid, snake, food):
        self.snake = snake
        self.food = food
        self.grid = grid
        self.head = self.snake.head
        self.food_pos = self.food.position
    
    def get_direction(self, algo= "Astar"):
        self.head = self.snake.head
        if algo == "greedy":
            a = self.greedy()
        elif algo == "Astar":
            path = self.Astar(self.snake.head, self.food.position)
            if path and len(path) > 1:
                next_step = path[1]
                dx = next_step[0] - self.head[0]
                dy = next_step[1] - self.head[1]
                a = (dx, dy)
            else:
                a = self.follow_tail()
        if not a or a == (0, 0):
            print("🛑 No valid move! Snake may crash.")
        if a == (1,0):
            return "D"
        elif a == (-1,0):
            return "A"
        elif a == (0,-1):
            return "W"
        elif a == (0,1):
            return "S"
        else:
            safe_dirs = []
            head = self.snake.head
            for neighbor in self.grid.get_neighbor_pos(head):
                if neighbor not in self.snake.body:
                    dx = neighbor[0] - head[0]
                    dy = neighbor[1] - head[1]
                    if (dx, dy) == (1, 0):
                        safe_dirs.append("D")
                    elif (dx, dy) == (-1, 0):
                        safe_dirs.append("A")
                    elif (dx, dy) == (0, -1):
                        safe_dirs.append("W")
                    elif (dx, dy) == (0, 1):
                        safe_dirs.append("S")
            return random.choice(safe_dirs) if safe_dirs else "D"

    def follow_tail(self):
        tail = self.snake.body[-1]
        path_to_tail = self.Astar(self.head, tail, True)
        if path_to_tail and len(path_to_tail) > 1:
            next_step = path_to_tail[1]
            dx = next_step[0] - self.head[0]
            dy = next_step[1] - self.head[1]
            return (dx, dy)
        else:
            return self.safe_random_move()
    
    def safe_random_move(self):
        safe_moves = []
        for neighbor in self.grid.get_neighbor_pos(self.head):
            if neighbor not in self.snake.body:
                dx = neighbor[0] - self.head[0]
                dy = neighbor[1] - self.head[1]
                safe_moves.append((dx, dy))
        return random.choice(safe_moves) if safe_moves else (0, 0)

    def greedy(self):
        neighbors = self.grid.get_neighbor_pos(self.head)
        cost_list = {}
        for i in neighbors:
            if i in self.snake.body:
                continue
            cost_list[i] = round(math.sqrt((self.food_pos[0] - i[0])**2 + (self.food_pos[1] - i[1])**2), 4)
        if not cost_list:
            return (0, 0)
        best_move = min(cost_list, key=cost_list.get) # type: ignore

        dx = best_move[0] - self.head[0]
        dy = best_move[1] - self.head[1]

        return (dx, dy)

    def heuristic(self, pos1, pos2):
        return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2
    
    def Astar(self, start_pos, goal_pos, ignore_tail = True):
        start = Node(None, start_pos)
        goal = Node(None, goal_pos)
        
        open_list = []
        closed_list = []
        
        open_list.append(start)
        
        while len(open_list) > 0:
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
            
            open_list.pop(current_index)
            closed_list.append(current_node)
            
            if current_node == goal:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                self.path = path[::-1]
                return self.path
            
            children = []

            for neighbor_pos in self.grid.get_neighbor_pos(current_node.position):
                if neighbor_pos in self.snake.body:
                    if not ignore_tail or neighbor_pos != self.snake.body[-1]:
                        continue
                new_node = Node(current_node, neighbor_pos)
                children.append(new_node)
                
            for child in children:
                if any(child == closed_child for closed_child in closed_list):
                    continue
                
                child.g = current_node.g + 1
                child.h = self.heuristic(child.position, self.food_pos)

                child.f = child.g + child.h
            
                if any(child == open_node and child.g > open_node.g for open_node in open_list):
                    continue
                
                open_list.append(child)
            
        self.path = []
        return []