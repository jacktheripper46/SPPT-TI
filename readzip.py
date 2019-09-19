from flask import Flask
from flask import jsonify
app = Flask(__name__)
@app.route('/agama')
def master_agama():
    f = open("agama.json", "r")
    for x in f:
        print(x)
        return jsonify(x)

if (__name__ == "__main__"):
    app.run(host = '0.0.0.0', port = 8001)