from alchemy.grimoire.spellbook import record_spell # noqa


def validate_ingredients(ingredients: str) -> str:

    ingredients_list: list[str] = ingredients.split()

    ingredients_base = [
        'fire', 'water', 'earth', 'air'
    ]
    count: int = 0

    for ingredient in ingredients_base:
        for word in ingredients_list:
            if ingredient == word:
                count += 1

    if count > 0:
        return (f'{ingredients} - VALID')
    else:
        return (f'{ingredients} - INVALID')
