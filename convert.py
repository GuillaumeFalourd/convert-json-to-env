import json
import sys
import os

env_file = os.getenv('GITHUB_ENV')

print("Start conversion")
filename = sys.argv[1]

# Opening JSON file
f = open(filename)
 
# returns JSON object as a dictionary
data = json.load(f)

for key, value in data.items():
    key = key.upper()
    print(key, value)
    with open(env_file, "a") as myfile:
        myfile.write(f"{key}={value}")

# Closing file
f.close()

print("End conversion")
