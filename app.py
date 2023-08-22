from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my python flak application"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6000))
    app.run(debug=True,host='0.0.0.0',port=port)
