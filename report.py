import numpy as np  
from scipy.spatial.distance import euclidean  
  
def find_surface_points(arr, color):  
    """  
    Find surface points of a given color.  
    A surface point has at least one neighbor with a different color.  
    """  
    z, y, x = arr.shape  
    surface_points = []  
    for i in range(z):  
        for j in range(y):  
            for k in range(x):  
                if arr[i, j, k] == color:  
                    # Check neighbors  
                    neighbors = []  
                    for dz, dy, dx in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:  
                        nz, ny, nx = i + dz, j + dy, k + dx  
                        if 0 <= nz < z and 0 <= ny < y and 0 <= nx < x:  
                            neighbors.append(arr[nz, ny, nx])  
                    if any(neighbor != color for neighbor in neighbors):  
                        surface_points.append((i, j, k))  
    return surface_points  
  
def largest_distance_between_surface_points(surface_points):  
    """  
    Calculate the largest distance between any two surface points.  
    """  
    max_distance = 0  
    point_pair = (None, None)  
    for i, point1 in enumerate(surface_points):  
        for point2 in surface_points[i+1:]:  
            distance = euclidean(point1, point2)  
            if distance > max_distance:  
                max_distance = distance  
                point_pair = (point1, point2)  
    return max_distance, point_pair  
  
def analyze_prism(arr, colors):  
    """  
    Analyze the prism for each color.  
    """  
    for color in colors:  
        surface_points = find_surface_points(arr, color)  
        if surface_points:  
            max_distance, point_pair = largest_distance_between_surface_points(surface_points)  
            print(f"Color {color}: Largest distance is {max_distance} between points {point_pair[0]} and {point_pair[1]}")  
            # Step 3 and 4 would require additional logic to find the largest distance of non-K contiguous color  
            # This can be approached by iterating through each dimension and looking for contiguous segments of the same color  
            # Then, calculate the distance for these segments.  
  
# Example usage  
Z, Y, X = 5, 5, 5  # Dimensions of the prism  
N = 2  # Number of items  
colors = [1, 2]  # Colors of the items  
arr = np.zeros((Z, Y, X))  # Initialize the prism with gas color K=0  
  
# Manually fill the array with item colors for demonstration  
# In a real scenario, this would be determined by the 3D scanner data  
arr[1:4, 1:4, 1:4] = 1  # Example item 1  
arr[0:3, 0:3, 0:3] = 2  # Example item 2  
  
analyze_prism(arr, colors)  

=============================
import json  

import openpyxl  
  
def lookupValue(searchString, fileName, sheetName, searchColumn, retValColumn):  
    # Load the specified sheet of the Excel file into a DataFrame  
    df = pd.read_excel(fileName, sheet_name=sheetName)  
      
    # Try to find the first row where the searchColumn matches the searchString  
    match = df[df[searchColumn] == searchString].head(1)  
      
    # If a match is found, return the value from the retValColumn of the same row  
    if not match.empty:  
        return match[retValColumn].values[0]  
      
    # If no match is found, return "None"  
    return "None"
"""  
# Example usage  
fileName = 'example.xlsx'  # Replace with your actual file name  
sheetName = 'Sheet1'  # Replace with your actual sheet name  
searchColumn = 1  # Assuming the search column is A (columns are 1-indexed in openpyxl)  
retValColumn = 2  # Assuming the return value column is B  
searchString = 'search_value'  # Replace with your actual search string  
  
result = lookupValue(searchString, fileName, sheetName, searchColumn, retValColumn)  
print(result)  
"""

def parse_json(input_file):  
    # Load the JSON data from the file  
    with open(input_file, 'r') as file:  
        data = json.load(file)  
  
    # Initialize an empty dictionary for the output  
    output = {}  
  
    # Function to recursively search for "Report" and "Result" keys  
    def search_data(d):  
        if isinstance(d, dict):  
            if "Report" in d and "Result" in d:  # Check if both keys exist in the current dict  
                report = d["Report"]  
                result = d["Result"]  
                output[report] = {}  # Initialize a dict for this report  
                for test, outcome in result.items():  
                    if outcome not in output[report]:  
                        output[report][outcome] = []  
                    output[report][outcome].append(test)  
            else:  
                for key in d:  
                    search_data(d[key])  # Recurse into the next level  
  
    # Start the recursive search from the top level  
    search_data(data)  
  
    return output  
  
# Assuming the input JSON file is named 'input.json'  
input_file = 'input.json'  
parsed_data = parse_json(input_file)  
  
# Print the output or write it to a file  
print(json.dumps(parsed_data, indent=2))  
  
# Optionally, write the output to a file  
with open('output.json', 'w') as file:  
    json.dump(parsed_data, file, indent=2)  
