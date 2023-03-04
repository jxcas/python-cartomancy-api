from flask import Flask

app = Flask(__name__)

@app.route("/suits")
def suits():
    return {"Diamonds":["Jack","Queen","King"]}

# tells server to launch along with port
if __name__ == '__main__':
    app.run(debug=True)