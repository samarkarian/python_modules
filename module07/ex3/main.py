from ex3.GameEngine import GameEngineClass
from ex3.AggressiveStrategy import AggressiveStrategyClass
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

    strategy = AggressiveStrategyClass()
    engine = GameEngineClass()
    engine.configure_engine(factory, strategy)
    result = engine.simulate_turn()
    print('\nTurn execution:')
    print(f"Strategy: {result['strategy']}")
    actions = {
        'cards_played': result['cards_played'],
        'mana_used': result['mana_used'],
        'targets_attacked': result['targets_attacked'],
        'damage_dealt': result['damage_dealt'],
    }
    print(f'Actions: {actions}')

    print('\nGame Report:')
    print(engine.get_engine_status())

    print(
        '\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!'
    )
