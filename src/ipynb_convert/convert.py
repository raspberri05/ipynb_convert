import json

def add(num):
  return num + 1

def convert_to_python(filename):
  count = 1

  with open(filename, mode="r", encoding="utf-8") as f:
    file = json.loads(f.read())

  new = open(filename.split('.')[0] + ".py", "x")
    
  for i in file["cells"]:
    # print("# cell " + str(count) + "\n")
    new.write("# cell " + str(count) + "\n\n")
    count += 1
    for j in i["source"]:
      # print(j)
      new.write(j)
    # print("\n")
    new.write("\n\n")