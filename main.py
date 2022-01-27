import requests

r = requests.get('http://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
# http://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=2
# print(r.json())  # if response type was set to JSON, then you'll automatically have a JSON response here


deck = r.json()
print("deck id: " + deck["deck_id"])


class MyDeck:
    def __init__(self, idhash):
        self.idhash = idhash

    basehtml = "http://deckofcardsapi.com/api/deck/"

    def drawcard(self, count):
        link = requests.get(self.basehtml + self.idhash + "/draw/?count=" + count)
        newcard = link.json()
        print(newcard['cards'][0]['code'])

    def shuffle(self, amount):
        if amount == "some":
            suffixlink = "?remaining=true"
        else:
            suffixlink = ""
        link = requests.get(self.basehtml + self.idhash + "/shuffle/" + suffixlink)
        link.json()
        print(amount + " cards have been shuffled")


d1 = MyDeck(deck["deck_id"])
d1.drawcard("1")
d1.shuffle("some")
d1.drawcard("1")
