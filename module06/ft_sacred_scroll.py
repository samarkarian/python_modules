from alchemy import elements
from _version import __version__

fire = elements.create_fire()
water = elements.create_water()


if __name__ == '__main__':
    print('\n=== Sacred Scroll Mastery ===\n')
    print('Testing direct module access:')

    print(fire)
    print(water)
    print(__version__)