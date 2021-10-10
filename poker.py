import random
from enum import Enum, auto
from typing import List, Set, Tuple


class Color(Enum):
    黑桃 = auto()
    紅心 = auto()
    方塊 = auto()
    梅花 = auto()


class Card:
    def __init__(self, color: Color, number: int) -> None:
        self.color = color
        self.number = number


class Deck:
    discard_cards: Set[Tuple] = set()

    def draw() -> Card:
        if (Deck.check_is_empty_deck()):
            raise Exception("排堆已空")

        chosen_card = Deck.choose_a_card()
        while (chosen_card in Deck.discard_cards):
            chosen_card = Deck.choose_a_card()

        Deck.discard_cards.add(chosen_card)
        return Card(chosen_card[0], chosen_card[1])

    def choose_a_card() -> Tuple:
        picked_color: Color = random.choice(Color._member_names_)
        picked_number: int = random.randint(1, 13)
        return (picked_color, picked_number)

    def check_is_empty_deck() -> bool:
        return len(Deck.discard_cards) >= 52


class PokerGame:
    cards: List[Card] = []
    how_many_cards: int

    def __init__(self, how_many_cards) -> None:
        self.how_many_cards = how_many_cards

    def game_start(self) -> None:
        for i in range(self.how_many_cards):
            self.cards.append(Deck.draw())

    def show_cards(self) -> None:
        number = 1
        for card in self.cards:
            print(f"{number}: {card.color}{card.number}", end="\n")
            number += 1

    def show_sorted_cards(self) -> None:
        sorted_cards: List[Card] = sorted(
            self.cards, key=lambda card: (card.number, card.color), reverse=True)
        number = 1
        for card in sorted_cards:
            print(f"{number}: {card.color}{card.number}", end="\n")
            number += 1


if __name__ == '__main__':
    new_game = PokerGame(52)
    new_game.game_start()
    new_game.show_sorted_cards()
