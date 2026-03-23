from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == 'add':
        return reduce(operator.add, spells)
    elif operation == 'multiply':
        return reduce(operator.mul, spells)
    elif operation == 'max':
        return reduce(max, spells)
    elif operation == 'min':
        return reduce(min, spells)
    else:
        raise ValueError(f"'{operation}' is not valid")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    fire_enchant = partial(base_enchantment, 50, 'fire')
    ice_enchant = partial(base_enchantment, 50, 'ice')
    lightning_enchant = partial(base_enchantment, 50, 'lightning')

    return {
        'fire_enchant': fire_enchant,
        'ice_enchant': ice_enchant,
        'lightning_enchant': lightning_enchant
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def dispatch(x):
        return x

    @dispatch.register
    def _(x: int) -> int:
        return x

    @dispatch.register
    def _(x: str) -> str:
        return x

    @dispatch.register
    def _(x: list) -> list:
        return x

    return dispatch


def main() -> None:
    print('Testing spell reducer...\n')

    try:
        print(f"Sum: {spell_reducer([1, 2, 3, 4], 'add')}")
        print(f"Product: {spell_reducer([1, 2, 3, 4], 'multiply')}")
        print(f"Max: {spell_reducer([1, 2, 3, 4], 'max')}")
        print(f"Min: {spell_reducer([1, 2, 3, 4], 'min')}")
    except ValueError as err:
        print(err)

    print('\nTesting partial enchanter...\n')

    def enchantment(power: int, element: str, target: str):
        return (
            f"{element} enchantment of power {power} on {target}"
        )

    enchantments: dict[str, Callable] = partial_enchanter(enchantment)
    print(enchantments['fire_enchant'](target='Frog'))
    print(enchantments['ice_enchant'](target='Cat'))
    print(enchantments['lightning_enchant'](target='Dog'))

    print('\nTesting memoized fibonacci...\n')

    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print('\nTesting spell dispatcher...\n')

    dispatcher = spell_dispatcher()

    print(f'Damage spell: {dispatcher(7)}')
    print(f"Enchantment: {dispatcher('Sword')}")
    print(f"Multi-cast: {dispatcher([7, 'Sword'])}")


if __name__ == '__main__':
    main()
