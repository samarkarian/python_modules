from functools import wraps
import time
import random
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()
        print(f'Casting {func.__name__}...')
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Spell completed in {end - start:.6f} seconds')

        return result

    return wrapper


@spell_timer
def fireball() -> str:
    return "Result: Fireball cast!"


def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            pow = args[2] if len(args) > 2 else args[0]
            if pow >= min_power:
                return func(*args, **kwargs)
            else:
                return 'Insufficient power for this spell'

        return wrapper
    return decorator


@power_validator(5)
def spell_power(power: int) -> str:
    return f'{power} is a sufficient power for this spell'


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper
    return decorator


@retry_spell(5)
def retry(power: int) -> str:
    if random.random() < 0.7:
        raise Exception("Spell fizzled!")
    return f"Fireball cast with power {power}!"


class MageGuild():
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        without_spaces: str = name.replace(" ", "")
        if len(name) >= 3 and without_spaces.isalpha():
            return True
        else:
            return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f'Successfully cast {spell_name} with {power} power'


def main() -> None:
    print('Testing spell timer...')
    print(fireball())

    print('\nTesting power validator...')
    print(spell_power(5))

    print('\nTesting retry spell...')
    print(retry(80))

    print('\nTesting MageGuild...')
    mage: MageGuild = MageGuild()
    print(mage.validate_mage_name('Bob'))
    print(mage.validate_mage_name('Bobby1'))
    print(mage.cast_spell('Lightning', 15))
    print(mage.cast_spell('Noname', 9))


if __name__ == '__main__':
    main()
