import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
#String in JSON mode

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
y["age"] = 50
print(y["age"])