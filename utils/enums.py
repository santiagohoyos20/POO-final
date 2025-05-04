from enum import Enum

class PlanetType(Enum):
    AGRI = 'Agri'
    CIVILISED = 'Civilised'
    DAEMON = 'Daemon'
    DEAD = 'Dead'
    DEATH = 'Death'
    FERAL = 'Feral'
    FEUDAL = 'Feudal'
    FORGE = 'Forge'
    FRONTIER = 'Frontier'
    HIVE = 'HIve'

class Status(Enum):
    ALIVE = 'Alive'
    DEAD = 'Dead'
    UNKNOWN = 'Unknown'

def decimal_to_roman(decimal_num):
    roman_numerals = {
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_num = ''
    for value, symbol in roman_numerals.items():
        while decimal_num >= value:
            roman_num += symbol
            decimal_num -= value

    return roman_num