# Pathfinding Algorithm for Road Networksst path between 2 points
 This Python script implements an A* algorithm to find the shortest path between two points in a road network, considering traffic conditions. The road network is represented by a CSV file containing road segments, their start and end coordinates, road names, road types, and traffic levels.

 ## How to Use
1. Prepare the CSV file: Create a CSV file with road segments' details, including start and end coordinates, road names, road types, and traffic levels.

2. Prepare the JSON file: Create a JSON file specifying the start and end points for which you want to find the shortest path.

3. Run the script: Execute the script and provide the names of the CSV and JSON files as input when prompted.

4. Output: The script will output the shortest path considering traffic conditions as a text file named "output.txt."

## CSV File Format
The CSV file should have the following columns:

1. Start X (float): X-coordinate of the start point of the road segment.
2. Start Y (float): Y-coordinate of the start point of the road segment.
3. End X (float): X-coordinate of the end point of the road segment.
4. End Y (float): Y-coordinate of the end point of the road segment.
5. Road Name (string): Name of the road segment.
6. Road Type (string): Type of the road segment (e.g., 'Highway', 'MainStreet', etc.).
7. Traffic (int): Traffic level of the road segment (integer value).

## JSON File Format
The JSON file should be like [THIS](start_end.json). Feel free to modify the start and end points.

## Output
 The output text file will contain the shortest path between the start and end points, considering traffic conditions. Each line in the file represents a road segment along the path.

Please note that if no path is found between the start and end points, the script will display "No path found" in the output.

## Credits
 This script uses the A* algorithm to find the shortest path, considering traffic conditions and road types. It calculates the heuristic based on the Euclidean distance between nodes and accounts for different road priorities and traffic levels in the pathfinding process.