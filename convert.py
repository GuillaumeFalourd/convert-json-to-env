import json
import sys
import os

env_file = os.getenv("GITHUB_ENV")

print("Start conversion")
filename = sys.argv[1]

# Opening JSON file
with open(filename, "r") as f:
    # Returns JSON object as a dictionary
    data = json.load(f)

# Add Key value to GITHUB_ENV (key will be UPPER CASE)
for key, value in data.items():
    key = key.upper()
    with open(env_file, "a") as myfile:
        myfile.write(f"{key}={value}" + '\n')

print("End conversion")
