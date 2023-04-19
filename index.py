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




def calculate_intersection_points(rows):
    list_of_nodes = []
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            ith = rows[i]
            jth = rows[j]
            x1 = float(ith[START_X])
            y1 = float(ith[START_Y])
            x2 = float(ith[END_X])
            y2 = float(ith[END_Y])
            x3 = float(jth[START_X])
            y3 = float(jth[START_Y])
            x4 = float(jth[END_X])
            y4 = float(jth[END_Y])

            if (y4 - y3) * (x2 - x1) == (y2 - y1) * (x4 - x3):
                continue

            if x1 == 5 and y1 == 5 and y4 == 4.25:
                n = 4

            x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
            y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

            if (x1 <= x <= x2 or x2 <= x <= x1) and (y1 <= y <= y2 or y2 <= y <= y1) and (x3 <= x <= x4 or x4 <= x <= x3) and (y3 <= y <= y4 or y4 <= y <= y3):

                if not any(node.x == x and node.y == y for node in list_of_nodes):
                    list_of_nodes.append(Node(x, y))
            
    for row in rows:

        if not any(node.x == float(row[START_X]) and node.y == float(row[START_Y]) for node in list_of_nodes):
            list_of_nodes.append(Node(float(row[START_X]), float(row[START_Y])))

        if not any(node.x == float(row[END_X]) and node.y == float(row[END_Y]) for node in list_of_nodes):
            list_of_nodes.append(Node(float(row[END_X]), float(row[END_Y])))

    for node in list_of_nodes:
        node.neighbors = get_neighbors(node, list_of_nodes, rows)
    
    return list_of_nodes

def get_neighbors(current: Node, list_of_nodes, rows):
    neighbors = []
    for node in list_of_nodes:
        if node.x == current.x and node.y == current.y:
            continue
        if node.x == current.x or node.y == current.y:
            neighbors.append([node, current.get_details(node, rows), current.get_distance(node)])
    return neighbors

def read_map(filename):
    rows = []
    with open(filename + '.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            rows.append(row)
    return rows

def read_JSON(filename, list_of_nodes):
    with open(filename  + '.json', 'r') as jsonfile:
        origin_to_destination = json.load(jsonfile)
    start_point = Node(origin_to_destination['START']['X'], origin_to_destination['START']['Y'])
    end_point = Node(origin_to_destination['END']['X'], origin_to_destination['END']['Y'])

    for node in list_of_nodes:
        if node.x == start_point.x and node.y == start_point.y:
            start_point = node
        if node.x == end_point.x and node.y == end_point.y:
            end_point = node

    return start_point, end_point


if __name__ == '__main__':
    student_number = '993613014'
    csv_file = input('enter the CSV file please:')
    json_file = input('enter the JSON file please:')
    rows = read_map(csv_file)
    list_of_nodes = calculate_intersection_points(rows)
    start_point, end_point = read_JSON(json_file, list_of_nodes)

    
