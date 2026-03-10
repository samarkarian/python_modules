from ex0.Card import CardClass


class SpellCardClass(CardClass):
    def __init__(
            self, name: str, cost: int,
            rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type: str = "Spell"

    def __repr__(self):
        return (f"{self.name} ({self.cost})")

    def play(self, game_state: dict) -> dict:

        game_state.update({'card_played': self.name})
        game_state.update({'mana_used': self.cost})
        game_state.update({'effect': self.effect_type})

        return (game_state)

    def resolve_effect(self, targets: list) -> dict:
        return {
            'effect': self.effect_type,
            'targets': targets,
        }
