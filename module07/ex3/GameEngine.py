from ex3.GameStrategy import GameStrategyClass
from ex3.CardFactory import CardFactoryClass


class GameEngineClass():
    def configure_engine(
            self,
            factory: CardFactoryClass, strategy: GameStrategyClass) -> None:
        pass

    def simulate_turn(self) -> dict:
        pass

    def get_engine_status(self) -> dict:
        pass
