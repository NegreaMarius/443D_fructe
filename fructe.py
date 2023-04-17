from flask import Flask
from lib import culoare

print("Fructe")

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = "<pre>"
    ret += "Informatii despre fructe:\n"
    ret += "</pre>"
    
    return ret
    
@app.route("/rodie/culoare", methods=['GET'])
def rodie_culoare():
    c = culoare.gaseste_culoare_rodie()
    ret = "<pre>"
    ret += f"Culoare rodie: {c}\n"
    ret += "</pre>"
    
    return ret 
    
