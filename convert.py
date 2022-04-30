import json
import sys

print("Start conversion")
print(sys.argv[1:])
filename = sys.argv(1)

# Opening JSON file
f = open(filename)
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
print(data)
 
# Closing file
f.close()

print("End conversion")
