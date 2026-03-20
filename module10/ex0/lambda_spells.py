def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    artifacts_sorted: list[dict] = sorted(
        artifacts, key=lambda x: x['power'], reverse=True
    )

    return (artifacts_sorted)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:

    mages_filter: list[dict] = list(filter(
        lambda x: x['power'] >= min_power, mages
    ))

    return (mages_filter)


def spell_transformer(spells: list[str]) -> list[str]:

    spells_map: list[str] = list(map(
        lambda x: '* ' + x + ' *', spells
    ))

    return (spells_map)


def mage_stats(mages: list[dict]) -> dict:

    min_int: list[dict] = min(
        mages, key=lambda x: x['power']
    )
    min_power: int = int(min_int['power'])

    max_int: list[dict] = max(
        mages, key=lambda x: x['power']
    )
    max_power: int = int(max_int['power'])

    avg_power = sum(map(lambda x: x['power'], mages)) / len(mages)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


def main() -> None:

    print('Testing artifact sorter...\n')
    artifacts: list[dict] = [
        {
            'name': 'Dragon',
            'power': 4,
            'type': 'medium'
        },
        {
            'name': 'Butterfly',
            'power': 2,
            'type': 'low'
        },
        {
            'name': 'Magic',
            'power': 6,
            'type': 'high'
        }
    ]
    new_artifacts: list[dict] = artifact_sorter(artifacts)
    for artifact in new_artifacts:
        print(f"{artifact['name']} ({artifact['power']})")

    print('\nTesting power filter...\n')
    min_power: int = 3
    mages: list[dict] = [
        {
            'name': 'James',
            'power': 4,
            'element': 'water'
        },
        {
            'name': 'Jason',
            'power': 2,
            'element': 'fire'
        },
    ]
    new_mages_collection: list[dict] = power_filter(mages, min_power)
    for mage in new_mages_collection:
        print(f"{mage['name']} ({mage['power']})")

    print('\nTesting spell transformer...\n')
    spells: list[str] = [
        'fireball', 'heal', 'shield'
    ]
    new_spells_list: list[str] = spell_transformer(spells)
    for spell in new_spells_list:
        print(str(spell))

    print('\nTesting mage stats...\n')
    stats: list[dict] = mage_stats(mages)
    print(
        f"Max power: {stats['max_power']}\n"
        f"Min power: {stats['min_power']}\n"
        f"Average power: {stats['avg_power']}"
    )


if __name__ == '__main__':
    main()
