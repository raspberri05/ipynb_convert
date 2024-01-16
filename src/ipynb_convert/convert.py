import json
import os

def convert_to_python(filename):
  count = 1

  with open(filename, mode="r", encoding="utf-8") as f:
    file = json.loads(f.read())

  python_filename = filename.split('.')[0] + ".py"

  if os.path.exists(python_filename):
    os.remove(python_filename)

  new = open(python_filename, "x")
    
  for i in file["cells"]: 
    new.write("# cell " + str(count) + "\n\n")
    count += 1
    cell_type = i["cell_type"]
    
    for j in i["source"]: 
      if cell_type == "code":
        new.write(j)
      if cell_type == "markdown":
        new.write("# " + j)

    new.write("\n\n")

def convert_to_ipynb(filename):
  with open(filename, mode="r", encoding="utf-8") as f:
    file = f.read()

  ipynb_filename = filename.split('.')[0] + ".ipynb"

  if os.path.exists(ipynb_filename):
    os.remove(ipynb_filename)
  
  new = open(ipynb_filename, "x")

  new.write('{}')