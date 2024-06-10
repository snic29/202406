import json  
import argparse  
  
def parse_config(config_lines):  
    """  
    Parse the configuration lines to extract patterns.  
      
    Parameters:  
    - config_lines: A list of strings, each representing a line in the configuration file.  
      
    Returns:  
    - A list of patterns to be used for matching against the JSON data.  
    """  
    patterns = []  
    for line in config_lines:  
        if line.strip():  # Remove any leading/trailing whitespace and check if line is not empty  
            patterns.append(line.strip())  # Add the cleaned line to the list of patterns  
    return patterns  
  
def match_pattern(data, pattern):  
    """  
    Recursively match the pattern in the given data and yield the matched results.  
      
    Parameters:  
    - data: The current level of JSON data being examined.  
    - pattern: The pattern string that specifies the path to match in the JSON data.  
      
    Yields:  
    - The data that matches the pattern.  
    """  
    keys = pattern.split('.')  # Split the pattern into keys based on '.'  
    current_data = data  
    for key in keys:  
        if key == "*":  # Wildcard, indicating any key at this level  
            if isinstance(current_data, dict):  # Ensure current data is a dictionary  
                for k, v in current_data.items():  # Iterate through all key-value pairs  
                    yield from match_pattern(v, '.'.join(keys[1:]))  # Recurse with remaining pattern  
                return  
        else:  
            if key in current_data:  # If the key is present in the current data  
                current_data = current_data[key]  # Move to the next level in the data  
            else:  
                return  # Key not found, stop processing this branch  
    yield current_data  # Yield the data that matches the pattern  
  
def extract_info(json_data, config_lines):  
    """  
    Extract and print information from json_data based on the config_lines.  
      
    Parameters:  
    - json_data: The parsed JSON data as a dictionary.  
    - config_lines: A list of configuration lines specifying what to extract.  
    """  
    patterns = parse_config(config_lines)  # Parse the configuration to get patterns  
    for pattern in patterns:  
        if "{" in pattern:  # Special handling for patterns with conditions (e.g., Result{"POS"})  
            base_pattern, value = pattern.split("{")  
            value = value.rstrip("}")  # Remove the closing brace  
            results = {}  
            for result in match_pattern(json_data, base_pattern):  # Match the base pattern  
                for k, v in result.items():  # Iterate through the matched results  
                    if v == value:  # Check if the value matches the condition  
                        if value not in results:  
                            results[value] = []  
                        results[value].append(k)  # Add the key to the results  
            for val, keys in results.items():  
                print(f"{val} : {','.join(keys)}")  # Print the results  
        else:  
            for result in match_pattern(json_data, pattern):  # For patterns without conditions  
                print(f"{pattern.split('.')[-1]} : {result}")  # Print the matched result  
        print("-----------")  
  
def main():  
    """  
    Main function to parse command-line arguments and extract information from JSON based on configuration.  
    """  
    parser = argparse.ArgumentParser(description="Parse JSON file based on configuration.")  
    parser.add_argument("-file", required=True, help="Path to the JSON file.")  
    parser.add_argument("-config", required=True, help="Path to the configuration file.")  
      
    args = parser.parse_args()  # Parse command-line arguments  
      
    with open(args.file, 'r') as json_file:  # Open and read the JSON file  
        json_data = json.load(json_file)  
      
    with open(args.config, 'r') as config_file:  # Open and read the configuration file  
        config_lines = config_file.readlines()  
      
    extract_info(json_data, config_lines)  # Extract and print the required information  
  
if __name__ == "__main__":  
    main()  # Execute the main function  
