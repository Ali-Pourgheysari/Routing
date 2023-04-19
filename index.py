import csv
import json
import heapq

START_X = 0
START_Y = 1
END_X = 2
END_Y = 3
ROAD_NAME = 4
ROAD_TYPE = 5
TRAFFIC = 6

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []
    
    def __lt__(self, other):
        return False

            
    def g_score(self, neighbor_node):
        node = Node(neighbor_node[0].x, neighbor_node[0].y)
        distance = self.get_distance(node)
        
        road_type_priority = 0
        traffic_priority = 7 - self.neighbors[1][2]
        road_type = self.neighbors[1][1]

        if road_type == 'Highway':
            road_type_priority = 1
        elif road_type == 'MainStreet':
            road_type_priority = 2
        else:
            road_type_priority = 3
        
        
        return distance * 0.5 + road_type_priority * 0.2 + traffic_priority * 0.3
    
    def get_path_name(self, node):
        path = None
        for neighbor in self.neighbors:
            if neighbor[0] == node:
                path = neighbor[1][0]
        return path

    def get_distance(self, node):
        return ((self.x - node.x) ** 2 + (self.y - node.y) ** 2) ** 0.5
    
    def get_details(self, node, rows):
        dx = self.x - node.x
        dy = self.y - node.y

        if dx == 0:
            m = 'inf'
            b = self.x
        else:
            m = (dy) / (dx)
            b = self.y - m * self.x

        for row in rows:
            x1 = float(row[START_X])
            y1 = float(row[START_Y])
            x2 = float(row[END_X])
            y2 = float(row[END_Y])

            m1 = 0
            b1 = 0
            dx = x1 - x2
            dy = y1 - y2
            if dx == 0:
                m1 = 'inf'
                b1 = x1
            else:
                m1 = (dy) / (dx)
                b1 = y1 - m1 * x1

            if m == m1 and b == b1:
                return row[ROAD_NAME], row[ROAD_TYPE], row[TRAFFIC]



