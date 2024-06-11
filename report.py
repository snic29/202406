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
