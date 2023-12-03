from json import load, dump

def load_json(file_name):
  try:
    with open(file_name, "r") as file:
      return load(file)
      
  except Exception as e:
    print("Open Json Error ->", e)
    return   # None

def save_json(file_name, data):
  try:
    with open(file_name, "w") as save:
      dump(data, save, ensure_ascii=False, indent=2)
      
  except: 
    print("Save Json Error!")

