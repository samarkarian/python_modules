from Card import CardClass


class CreatureCardClass(CardClass):
    def __init__(
            self,
            name: str,
            cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(self, name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        pass

    def attack_target(self, target) -> dict:
        pass


if __name__ == '__main__':

    player1 = CreatureCardClass('Fire Dragon', 5, 'Legendary', 7, 5)
    player1.get_card_info()
    # card1 = Card('Fire Dragon', 5, 'Legendary')
