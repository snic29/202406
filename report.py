import json  
  
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
