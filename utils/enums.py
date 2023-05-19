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