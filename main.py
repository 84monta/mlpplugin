import json

import quart
import quart_cors
from quart import request, jsonify
import tempfile
from pyscipopt import Model

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.post("/MLP/<string:username>")
async def solve(username):
    req_data = await request.get_json()
    fomulafile_txt = req_data["fomulafile"]
    with tempfile.NamedTemporaryFile(delete=False, suffix=".lp") as temp:
        temp.write(fomulafile_txt.encode())  
        temp_name = temp.name 
        
    model = Model()
    model.readProblem(temp_name)
    model.optimize()
    
    # #set result to dict
    result = {}
    result["status"] = model.getStatus()
    result["objval"] = model.getObjVal()
    #convert all variables and values to dict
    result["sol"] = {}
    for v in model.getVars():
        result["sol"][v.name] = model.getVal(v)
    response_txt = json.dumps(result)
    
    return jsonify(response_txt)

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
