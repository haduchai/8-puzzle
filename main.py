from copy import deepcopy
import time
# from graphviz import Digraph
# from IPython.display import display

# Định nghĩa Node
class Node:
    def __init__(self, state, level = 0, action=None, parent=None, fval=0):
        self.state = state
        self.level = level
        self.action = action
        self.parent = parent
        self.fval = fval

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.state]).replace('0', 'None')

    # các action có thể thực hiện
    def get_successors(self):
        successors = []
        actions = ['D', 'U', 'R', 'L']
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] 
        x, y = [(i, row.index('0')) for i, row in enumerate(self.state) if '0' in row][0]

        for action, nx, ny in zip(actions, dx, dy):
            if 0 <= x + nx < 3 and 0 <= y + ny < 3:
                new_state = deepcopy(self.state)
                new_state[x][y], new_state[x + nx][y + ny] = new_state[x + nx][y + ny], new_state[x][y]
                successors.append(Node(new_state, self.level + 1, action, self))

        return successors

class BFS:
    def __init__(self, start_node, goal_node1, goal_node2):
        self.start_node = start_node
        self.goal_node1 = goal_node1
        self.goal_node2 = goal_node2

    def process(self):
        start = time.time()
        queue = [self.start_node]
        visited = set()
        while queue:
            if time.time() - start > 60:
                print('Time out')
                return None
            node = queue.pop(0)
            visited.add(str(node.state))
            # print(node.state)
            if node.state == self.goal_node1.state or node.state == self.goal_node2.state:
                print('Goal state found')
                return node
            for successor in node.get_successors():
                if str(successor.state) not in visited:
                    queue.append(successor)


start_state = [[x for x in line.split()] for line in open('input.txt')]

goal_state1 = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

goal_state2 = [['1', '2', '3'],
              ['4', '5', '6'],
              ['7', '8', '0']]

start_node = Node(start_state)
goal_node1 = Node(goal_state1)
goal_node2 = Node(goal_state2)

puz = BFS(start_node, goal_node1, goal_node2)
# print(puz.h(goal_state2, goal_state2))
kq = puz.process()
print(kq.state)
print(kq.parent.state)
print(kq.parent.parent.state)