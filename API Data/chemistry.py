from config import load_json
import traceback, sys


def chemistry_search(chemical_name):
    data = load_json(file_name="elements.json")
    element = data["element_block"]
    
    if data:
      try:
        for name in data["elements"]:
          if chemical_name == name["symbol"]:
            data_ele = {key: val for key, val in name.items()}
            
            boil = data_ele["boil"] if data_ele["boil"] else "không có"
            melt = data_ele["melt"] if data_ele["melt"] else "không có"
            boil_t = round(data_ele["boil"]-273.2, 2) if data_ele["boil"] else "không có"
            melt_t = round(data_ele["melt"]-273.2, 2) if data_ele["melt"] else "không có"
            
            return {
              "name": data_ele["name"],
              "discovered_by": data_ele["discovered_by"],
              "atomic_block": data_ele["atomic_mass"],
              "atomic_number": data_ele["number"],
              "group": element[chemical_name][0],
              "cycle": element[chemical_name][1],
              "density": data_ele["density"],
              "boil": boil,
              "boil_temperature": boil_t,
              "melt": melt,
              "melt_temperature": melt_t,
              "electronegativity_pauling": data_ele["electronegativity_pauling"] if data_ele["electronegativity_pauling"] else "Không có",
              "category": data_ele["phase"],
              "class_block": data_ele["block"],
              "configuration": element[chemical_name][-1]
            }
          
      except Exception as e:
        print(e)
        #nơi này chỉ là tìm lỗi dòng -> file nào -> tên lỗi...
        name_error=str(sys.exc_info()[1])
        tb=sys.exc_info()[2]
        line_number = traceback.extract_tb(tb)[-1][1]
        print(line_number)
    
    return {"message": "Chemical not found"}
