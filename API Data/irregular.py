from requests import get

url = "https://gist.githubusercontent.com/Nguyen3006-IT/1ee510787a245a788f891874796231b7/raw/9b705179e1b02e68fb7482ce92de73e688a43930/bqt.json"

def irregular_search(verb:str):
    data = get(url).json()
    number = None
    for key, words in data["dic2"].items():
        if verb.lower() in words:
            number = key

    if number:
        return (
        data["dic1"][number][0],
        data["dic1"][number][1],
        data["dic1"][number][2],
        data["dic1"][number][3]
        )
    return 
    
  
