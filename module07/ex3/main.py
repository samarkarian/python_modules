# from ex3.GameEngine import GameEngineClass
# from ex3.AggressiveStrategy import AggressiveStrategy
# from ex3.CardFactory import CardFactoryClass
# from ex3.GameStrategy import GameStrategyClass
from ex3.FantasyCardFactory import FantasyCardFactoryClass
from typing import Any


if __name__ == '__main__':

    print('\n=== DataDeck Game Engine ===\n')

    print('Configuring Fantasy Card Game...')
    print('Factory: FantasyCardFactory')
    print('Strategy: AggressiveStrategy')

    factory = FantasyCardFactoryClass()
    hand: list[Any] = []

    hand.append(factory.create_creature('dragon'))
    hand.append(factory.create_creature('goblin'))
    hand.append(factory.create_spell('fireball'))
    hand.append(factory.create_artifact('mana_ring'))

    print(f'Available types: {factory.get_supported_types()}')

    print('\nSimulating aggressive turn...')
    print(hand)

    print('\nTurn execution:')
    print('Strategy: AggressiveStrategy')
