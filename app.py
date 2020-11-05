from flask import Flask, make_response

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
