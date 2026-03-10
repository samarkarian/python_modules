from ex3.CardFactory import CardFactoryClass
from ex3.GameStrategy import GameStrategyClass


class GameEngineClass():

    def __init__(self) -> None:
        self._factory: CardFactoryClass | None = None
        self._strategy: GameStrategyClass | None = None
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0
        self._hand: list = []

    def configure_engine(
            self,
            factory: CardFactoryClass,
            strategy: GameStrategyClass) -> None:
        self._factory = factory
        self._strategy = strategy
        self._hand = [
            factory.create_creature('dragon'),
            factory.create_creature('goblin'),
        ]
        self._cards_created = len(self._hand)

    def simulate_turn(self) -> dict:
        if self._factory is None or self._strategy is None:
            return {}

        result = self._strategy.execute_turn(self._hand, [])
        self._turns_simulated += 1
        self._total_damage += result.get('damage_dealt', 0)

        return result

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self._turns_simulated,
            'strategy_used': (
                self._strategy.get_strategy_name()
                if self._strategy else None
            ),
            'total_damage': self._total_damage,
            'cards_created': self._cards_created,
        }
