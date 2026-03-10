from ex3.CardFactory import CardFactoryClass
from ex3.GameStrategy import GameStrategyClass


class GameEngineClass():

    def __init__(self) -> None:
        self.factory: CardFactoryClass | None = None
        self.strategy: GameStrategyClass | None = None
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0
        self.hand: list = []

    def configure_engine(
            self,
            factory: CardFactoryClass,
            strategy: GameStrategyClass) -> None:

        self.factory = factory
        self.strategy = strategy

        self.hand = [
            factory.create_creature('dragon'),
            factory.create_creature('goblin'),
            factory.create_spell('fireball'),
            factory.create_artifact('mana_ring'),
        ]

        self.cards_created = len(self.hand)

    def simulate_turn(self) -> dict:

        if self.factory is None or self.strategy is None:
            return {}

        result = self.strategy.execute_turn(self.hand, [])
        self.turns_simulated += 1
        self.total_damage += result.get('damage_dealt', 0)

        return result

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': (
                self.strategy.get_strategy_name()
                if self.strategy else None
            ),
            'total_damage': self.total_damage,
            'cards_created': self.cards_created,
        }
