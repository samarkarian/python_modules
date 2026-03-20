def mage_counter() -> callable:
    counter: int = 0

    def counter_call() -> int:
        nonlocal counter
        counter += 1

        return (counter)

    return counter_call


def spell_accumulator(initial_power: int) -> callable:
    total_pow: int = initial_power

    def counter_power(amount: int) -> int:
        nonlocal total_pow
        total_pow += amount

        return (total_pow)

    return counter_power


def enchantment_factory(enchantment_type: str) -> callable:

    def enchantment(enchantment_name: str) -> str:
        return f'{enchantment_type} {enchantment_name}'

    return enchantment


def memory_vault() -> dict[str, callable]:
    store_dict: dict = {}

    def store(key: str, value: callable) -> None:
        store_dict[key] = value

    def recall(key: str) -> dict[str, callable]:
        if key in store_dict:
            return store_dict[key]
        else:
            return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


def main():
    print("Testing mage counter...\n")

    mc: callable = mage_counter()
    print(f'Call 1: {mc()}')
    print(f'Call 2: {mc()}')
    print(f'Call 3: {mc()}')

    print('\nTesting spell accumulator...\n')

    sa: callable = spell_accumulator(3)
    print(f'Call 1: {sa(3)}')
    print(f'Call 2: {sa(2)}')
    print(f'Call 3: {sa(1)}')

    print('\nTesting enchantment factory...\n')

    flaming: callable = enchantment_factory('Flaming')
    print(flaming('Sword'))

    frozen: callable = enchantment_factory('Frozen')
    print(frozen('Shield'))

    print('\nTesting memory vault...\n')

    memory: callable = memory_vault()
    memory["store"]("a", 10)
    print(memory["recall"]("a"))
    print(memory["recall"]("b"))


if __name__ == '__main__':
    main()
