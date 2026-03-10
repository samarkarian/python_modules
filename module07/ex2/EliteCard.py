from ex0.Card import CardClass
from ex2.Combatable import CombatableClass
from ex2.Magical import MagicalClass
from typing import Any


class EliteCardClass(CardClass, CombatableClass, MagicalClass):
    def __init__(self, name: str, cost: int, rarity: str,
                 combat_type: str, attack_power: int,
                 defense_power: int, spell: str, mana: int) -> None:
        super().__init__(name, cost, rarity)
        self.combat_type = combat_type
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.spell = spell
        self.mana = mana

    def attack(self, target) -> dict:

        attack_dict: dict[Any] = {}
        self.combat_type = 'melee'

        attack_dict = {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power,
            'combat_type': self.combat_type
        }
        return (attack_dict)

    def defend(self, incoming_damage: int) -> dict:

        defend_dict: dict[Any] = {}
        damage_blocked = self.defense_power - incoming_damage

        if damage_blocked < 0:
            damage_blocked = 0
        if damage_blocked > 0:
            self.still_alive: bool = True
        else:
            self.still_alive = False

        defend_dict = {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': damage_blocked,
            'still_alive': self.still_alive
        }
        return (defend_dict)

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.attack('Enemy'),
            'defense': self.defend(self.attack_power)
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:

        cast_spell_dict: dict[Any] = {
            'caster': spell_name,
            'spell': 'Fireball',
            'targets': targets,
            'mana_used': self.cost
        }
        return (cast_spell_dict)

    def channel_mana(self, amount: int) -> dict:

        self.mana -= self.cost
        self.mana += amount
        if self.mana < 0:
            self.mana = 0

        channel_mana_dict: dict[Any] = {
            'channeled': amount,
            'total_mana': self.mana
        }
        return (channel_mana_dict)

    def get_magic_stats(self) -> dict:
        return {
            'spell': self.cast_spell(self.name, ['Enemy1', 'Enemy2']),
            'mana': self.channel_mana(3)
        }

    def play(self, game_state: dict) -> dict:

        self.attack('Enemy')
        self.defend(10)
        self.cast_spell(self.name, ['Enemy1', 'Enemy2'])
        self.channel_mana(1)

        game_state = {
            'card_play': self.name,
            'is_alive': self.still_alive,
            'mana_total': self.mana
        }
        return (game_state)
