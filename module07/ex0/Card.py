from abc import ABC, abstractmethod


class CardClass(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return ({'hello': 3})

    def is_playable(self, available_mana: int) -> bool:
        pass
