from ex0.Card import CardClass
from ex2.Combatable import CombatableClass
from ex2.Magical import MagicalClass
from ex2.EliteCard import EliteCardClass


if __name__ == '__main__':
    print('\n=== DataDeck Ability System ===\n')

    card_class = (dir(CardClass))
    lst_card: list[str] = []

    for cla in card_class:
        if cla.startswith('_') is False:
            lst_card.append(cla)
    print(f'- Card: {lst_card}')

    combatable_class = (dir(CombatableClass))
    lst_combatable: list[str] = []

    for cla in combatable_class:
        if cla.startswith('_') is False:
            lst_combatable.append(cla)
    print(f'- Combatable: {lst_combatable}')

    magical_class = (dir(MagicalClass))
    lst_magical: list[str] = []

    for cla in magical_class:
        if cla.startswith('_') is False:
            lst_magical.append(cla)
    print(f'- Magical: {lst_magical}')

    print('\nPlaying Arcane Warrior (Elite Card):\n')
    print('Combat phase:')
    attack_power: int = 5
    arcane_warrior = EliteCardClass(
        'Arcane Warrior', attack_power, 'Legendary', 'melee', 7
    )
    print(f"Attack result: {arcane_warrior.attack('Enemy')}")
    print(f'Defense result: {arcane_warrior.defend(attack_power)}')
