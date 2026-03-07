from ex0.Card import CardClass
from ex2.Combatable import CombatableClass
from ex2.Magical import MagicalClass


class EliteCardClass(CardClass, CombatableClass, MagicalClass):
    def __init__(self, name: str, cost: int, rarity: str,
                 combat_type: str, attack_power: int,
                 defense_power: int) -> None:
        super().__init__(name, cost, rarity)
        self.combat_type = combat_type
        self.attack_power = attack_power
        self.defense_power = defense_power

    def attack(self, target) -> dict:
        self.combat_type = 'melee'
        return ({
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': self.combat_type
        })

    def defend(self, incoming_damage: int) -> dict:
        self.damage_taken: int = (self.defense_power - incoming_damage)

    def get_combat_stats(self) -> dict:
        pass

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        pass

    def play(self, game_state: dict) -> dict:
        pass
