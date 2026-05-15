from flask  import Flask, jsonify

app = Flask(__name__)


@app.route("/api/hello", methods=["GET"])
def hello_world():
    return jsonify({"mensagem": "Hello, World!"})


@app.route("/", methods=["GET"])
def raiz():
    return jsonify({"mensagem": "Voce esta na raiz. Va para: http://127.0.0.1:5000/api/hello"})


if __name__ == "__main__":
    app.run(debug=True)