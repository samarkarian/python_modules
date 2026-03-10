from ex4.TournamentCard import TournamentCardClass
from ex4.TournamentPlatform import TournamentPlatformClass
from typing import Any


if __name__ == '__main__':

    print('\n=== DataDeck Tournament Platform ===\n')
    print('Registering Tournament Cards...\n')

    platform = TournamentPlatformClass()

    fire_dragon = TournamentCardClass(
        'Fire Dragon', 5, 'Legend', 'dragon_001', 1200)
    platform.register_card(fire_dragon)

    ice_wizard = TournamentCardClass(
        'Ice Wizard', 3, 'Rare', 'wizard_001', 1150
    )
    platform.register_card(ice_wizard)

    interfaces = [
        base.__name__.replace("Class", "")
        for base in TournamentCardClass.__bases__
    ]

    print(f"{fire_dragon.name} (ID: {fire_dragon.card_id}):")
    print(f'Interfaces: {interfaces}')
    print(f'Rating: {fire_dragon.rating}')
    print(f'Record: {fire_dragon.wins}-{fire_dragon.losses}')
    print()
    print(f"{ice_wizard.name} (ID: {ice_wizard.card_id}):")
    print(f'Interfaces: {interfaces}')
    print(f'Rating: {ice_wizard.rating}')
    print(f'Record: {ice_wizard.wins}-{ice_wizard.losses}')

    print('\nCreating tournament match...')
    match: dict[Any] = platform.create_match(
                        fire_dragon.card_id, ice_wizard.card_id
                    )

    fire_dragon.play({})
    ice_wizard.play({})

    print(fire_dragon.attack(ice_wizard))

    print('\nTournament Leaderboard:')

    dragon_stat: dict[Any] = fire_dragon.get_tournament_stats()
    print(
        f"1. {dragon_stat.get('player')} - "
        f"Rating: {dragon_stat.get('rating')} "
        f"({dragon_stat.get('wins')}-{dragon_stat.get('losses')})"
    )

    wizard_stat: dict[Any] = ice_wizard.get_tournament_stats()
    print(
        f"2. {wizard_stat.get('player')} - "
        f"Rating: {wizard_stat.get('rating')} "
        f"({wizard_stat.get('wins')}-{wizard_stat.get('losses')})"
    )

    print('\nPlatform Report:')
    print(f'{platform.generate_tournament_report()}')

    print('\n=== Tournament Platform Successfully Deployed! ===')
    print('All abstract patterns working together harmoniously!')
