
from static_functions import *
import json


class A_Star_Buckets:
    def __init__(self, initial_states, goal_state):
        self.initial_states = initial_states  # array of string states
        self.goal_state = goal_state
        with open(f'Hanoi_PDB/hanoi_pdb_{num_disks-num_small_disk}.txt', "r") as file:
            file_data = file.read()
            self.database_big = json.loads(file_data)
        with open(f'Hanoi_PDB/hanoi_pdb_{num_small_disk}.txt', "r") as file:
            file_data = file.read()
            self.database_small = json.loads(file_data)
        self.heuristic_cache = {}
    
    def solve(self):
        frontier = []
        for state in self.initial_states:
            frontier = add_node_to_frontier(Node(state, None, 0, self.hur(state)), frontier)
        explored = []
        
        while len(frontier) > 0:
            cur_node = frontier.pop(0)
        
            if cur_node.state == self.goal_state:
                temp = len(explored)
                print(temp)
                return cur_node.g_n
                
            explored = add_node_to_explored(cur_node, explored)

            # create list of children
            child_list = self.get_children(cur_node)

            for child in child_list:
                if (not in_list(child, frontier)) and (not in_list(child, explored)):
                    frontier = add_node_to_frontier(child, frontier)
        
        return None
                    
    def get_solution(self, node):
        sol = []
        while node.parent is not None:
            sol.append(node.state)
            node = node.parent
        sol.reverse()
        return sol

    def get_children(self, cur_node):
        child_list = []
        
        min_disk_per_peg = [-1]*num_towers
        for peg in range(num_towers):
            for i, v in enumerate(cur_node.state):
                if int(v) == peg:
                    min_disk_per_peg[peg] = i
                    break
        
        for peg, disk in enumerate(min_disk_per_peg):
            for other_peg, other_disk in enumerate(min_disk_per_peg):
                if peg != other_peg and disk != -1:  # checks if not same peg and have a disk in that peg
                    if disk < other_disk or other_disk == -1:  # check if possible move
                        new_state = ""
                        for i, v in enumerate(cur_node.state):
                            if i == disk:
                                new_state += str(other_peg)
                            else:
                                new_state += v
                        child_list.append(Node(new_state, cur_node, cur_node.g_n + 1,
                                               self.hur(new_state)))  # creating child

        return child_list

    def hur(self, state):
        if state in self.heuristic_cache:
            return self.heuristic_cache[state]
        heuristic_value = self.database_big[state[num_small_disk:]][0] + self.database_small[state[:num_small_disk]][0]
        self.heuristic_cache[state] = heuristic_value
        return heuristic_value


def in_list(node, list1) -> bool:
    if len(list1) <= 0:
        return False
    for n in list1:
        if node.state == n.state:
            if node.g_n >= n.g_n:
                return True
    return False


def add_node_to_frontier(node, frontier):
    for i, n in enumerate(frontier):
        if node.g_n + node.h_n < n.g_n + n.h_n:
            frontier.insert(i, node)
            return frontier
    frontier.append(node)
    return frontier


def add_node_to_explored(node, explored):
    for i, n in enumerate(explored):
        if node.state == n.state:
            if node.g_n < n.g_n:
                explored[i] = node
                return explored
            else:
                return explored
    explored.append(node)
    return explored
