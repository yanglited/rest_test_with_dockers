from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/greet", methods=["GET"])
def greet():
    print("got request")
    return jsonify({"message": "Hi there, this is your response from the web service"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
