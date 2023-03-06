from cards import suit_meanings, number_meanings
import json, random

def get_reading(draw):
    cards = draw.json()["cards"]
    for i in range(len(cards)):
        keywords = get_keywords(cards[i])
        cards[i]['keywords'] = keywords
    return cards

def get_keywords(card):
    keywords = []
    suit = card["suit"]
    number = card["value"]
    keywords.extend(suit_meanings[suit]["keywords"])
    keywords.extend(number_meanings[number]["keywords"])
    random.shuffle(keywords)
    return keywords 