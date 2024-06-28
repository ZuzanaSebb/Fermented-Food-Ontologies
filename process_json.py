import os
import json

# Path to the JSON file
ontology_path = os.getenv('JSON_FILE_PATH')


try:
    with open(ontology_path, 'r') as f:
        ontology = json.load(f)
except FileNotFoundError:
    print(f"Error: JSON file '{ontology_path}' not found.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    exit(1)

# Get the comment body from environment variables
ontology_string = os.getenv('ONTOLOGY_STRING')
print(ontology_string)
# Define the regex pattern to match the comment format
import re

comment_regex = r'^([a-zA-Z]+)-([a-zA-Z]+)-([a-zA-Z]+)$'
match = re.match(comment_regex, ontology_string)

if not match:
    print('Comment format incorrect. Please use \'/approved ontology string:level1-level2-level3\'.')
    exit(1)

# Extract level1, level2, and level3 from the comment
level1, level2, level3 = match.groups()

# Update the ontology JSON structure
if level1 not in ontology:
    ontology[level1] = {}
if level2 not in ontology[level1]:
    ontology[level1][level2] = []
if level3 not in ontology[level1][level2]:
    ontology[level1][level2].append(level3)

# Write the updated JSON back to the file
try:
    with open(ontology_path, 'w') as f:
        json.dump(ontology, f, indent=2)
except Exception as e:
    print(f"Error writing JSON: {e}")
    exit(1)

print('Ontology updated successfully.')
