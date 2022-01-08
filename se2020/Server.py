from flask import Flask, jsonify

from se2020.morse import encode_morse

app = Flask(__name__)

@app.route("/")
def hello():
    payload = {"mensaje:": "Hola, mundo"}
    return jsonify(payload)


@app.route("/morse/<phrase>")
def encode(phrase):
    payload = {"resultado": encode_morse(phrase)}
    return jsonify(payload)


if __name__ == "__main__":
    app.run()
