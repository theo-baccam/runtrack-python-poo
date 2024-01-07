# Carte à attribut couleur (4), et valeur (1 à 13).
# La valeur de la carte et les points ne sont pas pareil
# figures 10 pontos, as 1 ou 11 points, ça sera déterminer par le jeu
from random import choice
from time import sleep


class Carte:
    def __init__(self, color, value):
        self.figures = {
            11: "Valet",
            12: "Reine",
            13: "Roi",
        }

        # J'utilise des attributs publics car c'est pas nécessaire que ça soit privé et aussi
        # ça rajoute des fonctions redondante.
        self.color = color
        self.value = value


class Person:
    def assess_value(self, value):
        if value >= 10:
            return 10
        return value

    def assess_total(self, hand):
        total = 0
        ace_number = 0
        for card in hand:
            points = self.assess_value(card.value)
            if points == 1:
                ace_number += 1
                continue
            if points >= 10:
                total += 10
                continue
            total += points
        totals_list = [total+(ace_number+10*i) for i in range(0, ace_number+1)]
        return totals_list


class Dealer(Person):
    def __init__(self, deck, player):
        super().__init__()
        self.out = False
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

    def show_cards(self):
        cards_status = "Le croupier a:\n- Une carte cachée (??)\n"
        for card in self.face_up_cards:
            points = self.assess_value(card.value)
            if points == 1:
                cards_status += f"- As de {card.color} (1 ou 10)\n"
                continue
            if card.value in card.figures:
                cards_status += f"- {card.figures[card.value]} de {card.color} ({points})\n"
                continue
            cards_status += f"- {card.value} de {card.color} ({points})\n"
        cards_status += f"En tout: {self.assess_total(self.face_up_cards)[0]} + ??"
        if len(self.face_up_cards) > 0:
            for total in self.assess_total(self.face_up_cards)[1:]:
                cards_status += f", {total} + ??"
        cards_status += f"\n"
        print(cards_status)


class Player(Person):
    def __init__(self):
        super().__init__()
        self.hand = []
        self.out = False
            

    def look_at_hand(self):
        hand_status = "Vous avez:\n"
        for card in self.hand:
            points = self.assess_value(card.value)
            if points == 1:
                hand_status += f"- As de {card.color} (1 ou 10)\n"
                continue
            if card.value in card.figures:
                hand_status += f"- {card.figures[card.value]} de {card.color} ({points})\n"
                continue
            hand_status += f"- {card.value} de {card.color} ({points})\n"
        hand_status += f"En tout: {self.assess_total(self.hand)[0]}"
        for total in self.assess_total(self.hand)[1:]:
            hand_status += f", {total}"
        hand_status += f"\n"
        print(hand_status)


class Jeu:
    def __init__(self):
        self.color_list = ("Pic", "Carreaux", "Trèfles", "Coeurs")
        self.deck = self.make_blackjack_deck()

        self.player = Player()
        self.dealer = Dealer(self.deck, self.player)
        
        self.check_player_bust()
        self.check_player_blackjack()

        self.check_dealer_out()

        while True:
            print(self.dealer.assess_value(self.dealer.face_down_card[0].value))
            self.dealer.show_cards()
            self.player.look_at_hand()

            self.input_loop()

            self.check_player_bust()
            self.check_player_blackjack()

            
            if not self.dealer.out:
                self.dealer.draw_card(self.deck, self.dealer.face_up_cards)
                print("Le croupier pioche une carte.")
                sleep(0.25)

            self.check_dealer_out()

            if self.dealer.out and self.player.out:
                max_dealer_total = (
                    max(self.dealer.assess_total(self.dealer.face_up_cards)) + 
                    self.dealer.assess_value(self.dealer.face_down_card[0].value)
                )
                max_player_total = max(self.player.assess_total(self.player.hand))
                print(
                    f"Dealer: {max_dealer_total}\n"
                    f"Player: {max_player_total}\n"
                )
                if max_dealer_total == max_player_total:
                    print("Egalité")
                elif max_dealer_total > 21 and max_player_total > 21:
                    print("Egalité")
                elif max_dealer_total > 21:
                    print("Le croupier est au-dessus de 21, le joueur gagne.")
                elif max_player_total > 21:
                    print("Le joueur est au-dessus de 21, le croupier gagne.")
                elif max_dealer_total == 21:
                    print("Le croupier a Blackjack et gagne")
                elif max_player_total == 21:
                    print("Le joueur a Blackjack et gagne")
                elif max_dealer_total > max_player_total:
                    print("Le croupier a plus que le joueur et gagne.")
                elif max_player_total > max_dealer_total:
                    print("Le joueur a plus que le croupier et gagne.")
                break

    def make_blackjack_deck(self):
        deck = []
        for color in self.color_list:
            for number in range(1, 13+1):
                carte = Carte(color, number)
                deck.append(carte)
        return deck

    def input_loop(self):
        if not self.player.out:
            choice = input("1) Prendre une carte\n2) Rester\n")
            if choice == "1":
                self.dealer.draw_card(self.deck, self.player.hand)
                print("Le joueur a pioché une carte")
            elif choice == "2":
                self.player.out = True
                print("Le joueur reste")
            else:
                print("Choix invalide")
            print("\n")

    def check_player_bust(self):
        if min(total > 21 for total in self.player.assess_total(self.player.hand)):
            self.player.out = True

    def check_player_blackjack(self):
        if any(total == 21 for total in self.player.assess_total(self.player.hand)):
            self.player.out = True

    def check_dealer_out(self):
        if (any((
            total + self.dealer.assess_value(self.dealer.face_down_card[0].value) >= 17 
            for total in self.dealer.assess_total(self.dealer.face_up_cards)))
        ):
            self.dealer.out = True


def main():
    blackjack = Jeu()

if __name__ == "__main__":
    main()
