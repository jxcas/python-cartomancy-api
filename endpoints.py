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


# TODO:
# basic card functionality from Deck of Cards API
    # shuffle
    # draw (3 spread)
    # display drawn cards
# dict with cartomancy meanings
# one-to-one connection w Deck of Cards by suit/number
# return combined object
    # spread: {
    #   first_card: {
    #       "code": ""
    #       "value": ""
    #       "suit": ""
    #       "position_name": ""  # this is set by the client-side request?
    #       "keywords": ["","",""]  # possible this is actually determined by the value and suit, calling on 
    #       "description": ["","",""]
    # }}