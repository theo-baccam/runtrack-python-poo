# Carte à attribut couleur (4), et valeur (1 à 13).
# La valeur de la carte et les points ne sont pas pareil
# figures 10 pontos, as 1 ou 11 points, ça sera déterminer par le jeu
from random import choice


class Carte:
    def __init__(self, color, value):
        # J'utilise des attributs publics car c'est pas nécessaire que ça soit privé et aussi
        # ça rajoute des fonctions redondante.
        self.color = color
        self.value = value


class Dealer:
    def __init__(self, deck, player):
        self.face_down_card = []
        self.face_up_cards = []

        self.draw_card(deck, self.face_down_card)
        self.draw_card(deck, self.face_up_cards)

        self.draw_card(deck, player.hand)
        self.draw_card(deck, player.hand)

    def draw_card(self, draw_pile, destination):
        random_card = choice(draw_pile)
        destination.append(random_card)
        draw_pile.remove(random_card)
        print(random_card.color, random_card.value)


class Player:
    def __init__(self):
        self.hand = []

    def assess_value(self, value):
        if value >= 10:
            return 10
        return value

    def assess_total(self):
        totals_list = []
        total = 0
        ace_number = 0
        for card in self.hand:
            points = self.assess_value(card.value)
            if points == 1:
                ace_number += 1
                continue
            if points >= 10:
                total += 10
                continue
            total += points
        if ace_number == 0:
            totals_list = [total]
        elif ace_number == 1:
            totals_list = [total+1, total+11]
        elif ace_number == 2:
            totals_list = [total+2, total+12, total+22]
        elif ace_number == 3:
            totals_list = [total+3, total+13, total+23, total+33]
        elif ace_number == 4:
            totals_list = [ total+4, total+14, total+24, total+34, total+44 ]
        return totals_list

            

    def look_at_hand(self):
        figures = {
            11: "Valet",
            12: "Reine",
            13: "Roi",
        }

        hand_status = "Vous avez:\n"
        for card in self.hand:
            points = self.assess_value(card.value)
            if points == 1:
                hand_status += f"- As de {card.color} (1 ou 10)\n"
                continue
            if card.value in figures:
                hand_status += f"- {figures[card.value]} de {card.color} ({points})\n"
                continue
            hand_status += f"- {card.value} de {card.color} ({points})\n"
        hand_status += f"En tout:{self.assess_total()}"
        print(hand_status)


class Jeu:
    def __init__(self):
        self.color_list = ("Pic", "Carreaux", "Trèfles", "Coeurs")
        self.deck = self.make_blackjack_deck()

        self.player = Player()
        self.dealer = Dealer(self.deck, self.player)
        
        while True:
            choice = input("")
            self.player.look_at_hand()

    def make_blackjack_deck(self):
        deck = []
        for color in self.color_list:
            for number in range(1, 13+1):
                carte = Carte(color, number)
                deck.append(carte)
        return deck

def main():
    blackjack = Jeu()

if __name__ == "__main__":
    main()
