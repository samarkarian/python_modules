from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs):
        s1, s2 = spell1(*args, **kwargs), spell2(*args, **kwargs)
        return (s1, s2)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(*args, **kwargs):
        original = base_spell(*args, **kwargs)
        amplified = original * multiplier
        return (f"Original: {original}, Amplified: {amplified}")

    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def condition_spell(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)

        return 'Spell fizzled'

    return condition_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs):
        res: list[str] = []
        for spell in spells:
            res.append(spell(*args, **kwargs))
        return res

    return sequence


def main() -> None:
    print('- Testing spell combiner...\n')

    def spell1() -> str:
        return "Fireball hits Dragon"

    def spell2() -> str:
        return "Heals Dragon"

    sc: Callable = spell_combiner(spell1, spell2)
    print(f'Combined spell result: {sc()}')

    print('\n- Testing power amplifier...\n')

    def base_spell() -> int:
        return (5)

    pa: Callable = power_amplifier(base_spell, 10)
    print(pa())

    print('\n- Testing conditional caster...\n')

    def condition(cost: int) -> bool:
        if cost < 5:
            return True
        else:
            return False

    def spell(cost: int) -> str:
        return f'Spell has succeeded, cost is {cost}'

    cc: Callable = conditional_caster(condition, spell)
    print(cc(4))

    print('\n- Testing spell sequence...\n')

    ss: Callable = spell_sequence([spell1, spell2])

    print(f'Sequence: {ss()}')


if __name__ == '__main__':
    main()
