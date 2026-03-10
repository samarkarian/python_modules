from ex0.Card import CardClass
import random


class DeckClass():
    def __init__(self) -> None:
        self.cards: list[CardClass] = []

    def add_card(self, card: CardClass) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> CardClass:
        return (random.choice(self.cards))

    def get_deck_stats(self) -> dict:
        avg_cost: float = round(sum(
                    [card.cost for card in self.cards]
                ) / len(self.cards), 2)

        return (
            {
                'total_cards': len(self.cards),
                'creatures': sum(
                    [card.type == 'Creature' for card in self.cards]
                ),
                'spells': sum(
                    [card.type == 'Spell' for card in self.cards]
                ),
                'artifacts': sum(
                    [card.type == 'Artifact' for card in self.cards]
                ),
                'avg_cost': avg_cost,
            }
        )
