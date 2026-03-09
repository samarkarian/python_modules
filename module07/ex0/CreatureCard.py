from ex0.Card import CardClass


class CreatureCardClass(CardClass):
    def __init__(
            self,
            name: str,
            cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type: str = "Creature"

    def __repr__(self):
        return (f"{self.name} ({self.cost})")

    def play(self, game_state: dict) -> dict:
        game_state.update({'card_played': self.name})
        game_state.update({'mana_used': self.cost})
        game_state.update({'effect': 'Creature summoned to battlefield'})
        return (game_state)

    def get_card_info(self) -> dict:
        fire_dragon_info: dict = {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': self.type,
            'attack': self.attack,
            'health': self.health,
        }
        return (fire_dragon_info)

    def is_playable(self, available_mana: int) -> bool:
        if available_mana > 4:
            return True
        else:
            return False

    def attack_target(self, target: str) -> dict:
        return (
            {
                'attacker': self.name,
                'target': target,
                'damage_dealt': self.attack,
                'combat_resolved': True
            }
        )
