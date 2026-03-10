from ex0.Card import CardClass


class ArtifactCardClass(CardClass):
    def __init__(
            self,
            name: str, cost: int, rarity: str,
            durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type: str = "Artifact"

    def __repr__(self):
        return (f"{self.name} ({self.cost})")

    def play(self, game_state: dict) -> dict:
        game_state.update({'card_played': self.name})
        game_state.update({'mana_used': self.cost})
        game_state.update({'effect': self.effect})
        return (game_state)

    def activate_ability(self) -> dict:
        return {}
