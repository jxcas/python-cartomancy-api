from flask import Flask
import requests, json
from cards import suit_meanings, value_meanings, special_combos
from get_reading import get_reading

app = Flask(__name__)

@app.route("/deck")
def deck():
    get_deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    return get_deck.json()

@app.route("/draw_card")
def draw_card():
    draw = requests.get("https://deckofcardsapi.com/api/deck/new/draw/?count=1")
    return draw.json()

@app.route("/draw_three")
def draw_three():
    get_deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    deck_id = get_deck.json()["deck_id"]
    draw = requests.get("https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=3".format(deck_id=deck_id))

    spread = get_reading(draw)

    return draw.json()
    

@app.route("/suits")
def suits():
    return suit_meanings;

@app.route("/numbers")
def numbers():
    return value_meanings;

@app.route("/special")
def special():
    return special_combos;



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