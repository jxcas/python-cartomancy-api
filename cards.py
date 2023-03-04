from flask import Flask
import requests, json

app = Flask(__name__)

@app.route("/suits")
def suits():
    return {"Diamonds":["Jack","Queen","King"]}

@app.route("/deck")
def deck():
    get_deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    return get_deck.json()

# tells server to launch along with port
if __name__ == '__main__':
    app.run(debug=True)