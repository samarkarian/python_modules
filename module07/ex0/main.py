from ex0.CreatureCard import CreatureCardClass

if __name__ == '__main__':

    print('\n=== DataDeck Card Foundation ===\n')
    print('Testing Abstract Base Class Design:\n')

    print('CreatureCard Info:')
    fire_dragon = CreatureCardClass('Fire Dragon', 5, 'Legendary', 7, 5)
    print(fire_dragon.get_card_info())

    print('\nPlaying Fire Dragon with 6 mana available:')
    print(f'Playable: {fire_dragon.is_playable(6)}')

    print(f'Play result: {fire_dragon.play({})}')

    print('\nFire Dragon attacks Goblin Warrior:')
    print(f"Attack result: {fire_dragon.attack_target('Goblin Warrior')}")

    print('\nTesting insufficient mana (3 available):')
    print(f'Playable: {fire_dragon.is_playable(3)}')

    print('\nAbstract pattern successfully demonstrated!')
