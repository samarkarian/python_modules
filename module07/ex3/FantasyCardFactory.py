from ex0.Card import CardClass
from ex3.CardFactory import CardFactoryClass
from ex0.CreatureCard import CreatureCardClass
from ex1.SpellCard import SpellCardClass
from ex1.ArtifactCard import ArtifactCardClass
import random
from typing import Any


class FantasyCardFactoryClass(CardFactoryClass):

    def __init__(self) -> None:
        self.creatures_list: list[Any] = []
        self.spells_list: list[Any] = []
        self.artifacts_list: list[Any] = []

    def create_creature(
                    self,
                    name_or_power: str | int | None = None
                ) -> CardClass:

        self.creatures_list.append(name_or_power)

        creature_card = CreatureCardClass(
            name_or_power, random.randint(1, 5), 'Legend',
            random.randint(1, 5), random.randint(1, 5)
        )

        return (creature_card)

    def create_spell(
                    self,
                    name_or_power: str | int | None = None
                ) -> CardClass:

        self.spells_list.append(name_or_power)

        spell_card = SpellCardClass(
            name_or_power, random.randint(1, 5),
            'High', 'Deal 3 damage to target'
        )

        return (spell_card)

    def create_artifact(
                    self,
                    name_or_power: str | int | None = None
                ) -> CardClass:

        self.artifacts_list.append(name_or_power)

        artifact_card = ArtifactCardClass(
            name_or_power, random.randint(1, 5), 'Medium',
            random.randint(1, 5), 'Permanent: +1 mana per turn'
        )

        return (artifact_card)

    def create_themed_deck(self, size: int) -> dict:

        deck: list[Any] = []
        deck = self.creatures_list + self.spells_list + self.artifacts_list
        size = len(deck)

        return {'deck': deck, 'size': size}

    def get_supported_types(self) -> dict:

        return ({
            'creatures': self.creatures_list,
            'spells': self.spells_list,
            'artifacts': self.artifacts_list
        })
