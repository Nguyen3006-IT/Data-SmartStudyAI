from flask import Flask, request, jsonify
from irregular import irregular_search
from chemistry import chemistry_search
from engWords import find_word, selectFirst, selectOut

app = Flask("__name__")

@app.route("/", methods=["GET"])
def home():
    return "api data for Bot"

@app.route("/irregular", methods=["GET"])
def irregular():
    verb = request.args.get("verb")
    irregular = irregular_search(verb=verb)
    
    if irregular:
        return jsonify({
            "v1": irregular[0],
            "v2": irregular[1],
            "v3": irregular[2],
            "means": irregular[3]
        }), 200
    
    return ""

@app.route("/chemistry", methods=["GET"])
def chemistry():
    try: 
        name = request.args.get("chemical")
        result_chemistry = chemistry_search(chemical_name=name.title())
        if not result_chemistry:
            return jsonify({"message": "Chemical not found"}), 400
    
        return jsonify(result_chemistry), 200
    except: 
        return jsonify({"message": "Error !"}), 500


@app.route("/vocabulary", methods=["GET"])
def vocabulary():
    try: 
        word = request.args.get("word")
        result = find_word(word=word) # trả về dưới dạng dict
        
        if not result:
            return jsonify({"message": "Word not found"}), 400
    
        return jsonify(result), 200
    except: 
        return jsonify({"message": "Error !"}), 500



@app.route("/matchEng", methods=["POST"])
def matchEng():
    try: 
        data = request.get_json()
        if data:
            char = data["char"]
            location = data["location"]
            if location == "first":
                result = selectFirst(charFirst=char)
            else:
                result = selectOut(charOut=char)
        else: 
            return jsonify({"message": "Error !"}), 500


        if not result:
            return jsonify(result), 400
        return jsonify(result), 200
    except: 
        return jsonify({"message": "Error !"}), 500


#run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)