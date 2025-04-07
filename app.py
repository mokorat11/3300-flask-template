from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

app.route("/sum")
def sum():
    a = 5
    b = 10
    c = a + b
    return f"The sum of {a} and {b} is {c}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)