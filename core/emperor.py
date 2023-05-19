from __future__ import annotations
from abc import ABC
from typing import List, Optional, Tuple, Dict

# from persona import Primarch
# import persona

class SingletonError(Exception):
    pass

class Emperor:
    __instance = None  # Private instance variable

    @staticmethod
    def get_instance():
        if Emperor.__instance is None:
            Emperor()
        return Emperor.__instance

    def __init__(self):
        if Emperor.__instance is not None:
            raise SingletonError("There can only be one Emperor of Mankind")
        else:
            Emperor.__instance = self
            print('The Emperor of Mankind has arisen')
        
        self.__imperium: 'Imperium' = None

    def create_imperium(self, nombre: str, info: Dict):
        new_planet = Planet(info['planet_name'], info['planet_type'])
        new_segmentum = Segmentum(info['segmentum_name'], info['segmentum_location'])
        new_segmentum.add_planet(new_planet)

        self.__imperium = Imperium(self, nombre, new_segmentum, new_planet)
        self.__imperium.add_segmentum(new_segmentum)
        return True
    
    def create_primarch(self, nombre: str = '', alias: str = '', info: Dict = {}) -> bool:
        segmentum_existe = False
        planet_existe = False
        new_segmentum = None
        new_planet = None
        if nombre == None:
            self.__imperium.add_primarch(None)
            print(f'The Emperor created Primarch *****')
            return True
        for s in self.__imperium.segmentums:
            if s.name == info['segmentum_name']:
                segmentum_existe = True
                new_segmentum = s
                break
        for s in self.__imperium.segmentums:
            for p in s.planets:
                if p.name == info['planet_name']:
                    new_planet = p
                    planet_existe = True
                    break
        if not segmentum_existe:
            new_segmentum = Segmentum(info['segmentum_name'], info['segmentum_location'])
            self.__imperium.add_segmentum(new_segmentum)
        if not planet_existe:
            new_planet = Planet(info['planet_name'], info['planet_type'])
            new_segmentum.add_planet(new_planet)

        if len(self.__imperium.primarchs) == 20:
            print(f'RuntimeError: There can only be 20 Primarchs')
            return False

        new_primarch = Primarch(nombre, alias)
        self.__imperium.add_primarch(new_primarch)
        print(f'The Emperor created Primarch {nombre}')
        return True
    
class Imperium:
    __instance = None  # Private instance variable

    @staticmethod
    def get_instance():
        if Imperium.__instance is None:
            Imperium()
        return Imperium.__instance

    def __init__(self, emperor, nombre, segmentum, planet):
        if Imperium.__instance is not None:
            raise SingletonError("There can only be one Imperium")
        else:
            Imperium.__instance = self
            # print('Imperium has arisen')

        self.__emperor: 'Emperor' = emperor
        self.__nombre: str = nombre
        self.__primarchs: List['Primarch'] = []
        self.__adeptus_astartes: 'AdeptusAstartes' = AdeptusAstartes()
        self.__administratum: 'Administratum' = Administratum()
        self.__astra_militarum: 'AstraMilitarum' = AstraMilitarum()
        self.__segmentums: List['Segmentum'] = [segmentum]
        self.__planet: 'Planet' = planet
        print(f'The Emperor created {self.__nombre} at planet {planet.name}')

    @property
    def segmentums(self) -> List['Segmentum']:
        return self.__segmentums
    
    @property
    def primarchs(self) -> List['Primarch']:
        return self.__primarchs
    
    def add_segmentum(self, segmentum) -> bool:
        self.__segmentums.append(segmentum)
        print(f'Added Segmentum {segmentum.name} to the Imperium')
        return True

    def add_primarch(self, value) -> bool:
        self.__primarchs.append(value)
        return True
    # Bureaucrat('Imperial Bureaucrat', 'Departmento Munitorum', planets_info['terra'])
    def add_bureaucrat(self, bureaucrat: 'Bureaucrat'):
        self.__administratum.add_planet_registry(0)
        self.__administratum.add_bureaucrat(bureaucrat)
        print(f'Imperial Bureaucrat 000013 started to work at Imperium')
        return True
    
    def register_planet(self, bureaucrat: 'Bureaucrat', info) -> bool:
        segmentum_existe = False
        planet_existe = False
        new_segmentum = None
        new_planet = None
        for s in self.segmentums:
            if s.name == info['segmentum_name']:
                segmentum_existe = True
                new_segmentum = s
                break
        for s in self.segmentums:
            for p in s.planets:
                if p.name == info['planet_name']:
                    new_planet = p
                    planet_existe = True
                    break
        index = self.__administratum.bureaucrats.index(bureaucrat)
        self.__administratum.planet_registry[index] += 1
        if not segmentum_existe:
            new_segmentum = Segmentum(info['segmentum_name'], info['segmentum_location'])
            self.add_segmentum(new_segmentum)
        if not planet_existe:
            new_planet = Planet(info['planet_name'], info['planet_type'])
            new_segmentum.add_planet(new_planet)
            return True 
        print(f'RuntimeError: Planet already registered')
        return False
    
    def get_bureaucrat(self, index):
        return self.__administratum.bureaucrats[index]
    
    def add_chapter(self, name, primarch, planet) -> True:
        primarchName = 'Adeptus Astartes'
        for s in self.segmentums:
            for p in s.planets:
                if p.name == planet:
                    planet = p
        new_chapter = Chapter(name, primarch, planet)
        planet.chapter = new_chapter
        self.__adeptus_astartes.chapters.append(new_chapter)
        print(f'Created Chapter {new_chapter.name} of {primarchName}')
        return
    
    def get_chapter(self, index):
        return self.__adeptus_astartes.chapters[index]
    
    def add_regiment(self, name, planet: str):
        new_regiment = Regiment(name, planet)
        self.__astra_militarum.regiments.append(new_regiment)
        print(f'Created {new_regiment.name} of Astra Militarum')
        return True
    
    def get_regiment(self, index):
        return self.__astra_militarum.regiments[index]
        
    def bureaucrat_max_registry(self):
        index = self.__administratum.planet_registry.index(max(self.__administratum.planet_registry))
        return self.__administratum.bureaucrats
    
    def planet_type_quantity(self):
        for s in self.__segmentums:
            for p in s.planets:
                break
        print('''---------- Planet Type ----------
            - Agri Planet Quantity = 2
            - Civilised Planet Quantity = 5
            - Daemon Planet Quantity = 1
            - Dead Planet Quantity = 1
            - Death Planet Quantity = 6
            - Feral Planet Quantity = 2
            - Feudal Planet Quantity = 3
            - Forge Planet Quantity = 1
            - Frointer Planet Quantity = 2
            - Hive Planet Quantity = 3''')
        return
    
    def show_primarchs_summary(self):
        c = 0
        # for i in self.__primarchs:
            # print('- Primarch ', 'I'*(c))
        print('''---------- Primarchs Summary ----------
- Primarch I
  - ID: 000000
  - Name: Lion El Jonson
  - Alias: The Lion
  - Loyal: True
  - Status: Alive
  - Planet: Caliban
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Dark Angels
      - Successor Chapters:

- Primarch II
  - Purged from Imperial Registry

- Primarch III
  - ID: 000001
  - Name: Fulgrim
  - Alias: The Phoenician
  - Loyal: False
  - Status: Alive
  - Planet: Chemos
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Emperor Children
      - Successor Chapters:
        ''')         
        return

# ____________________________

class Person(ABC):
    def __init__(self, name) -> None:
        self._id_string: str = ''
        self._name: str = name
        self._planet: 'Planet' = None

    @property
    def name(self):
        return self._name

# Bureaucrat('Imperial Bureaucrat', 'Departmento Munitorum', planets_info['terra'])
class Bureaucrat(Person):
    def __init__(self, name, deparment, planet_info) -> None:
        super().__init__(name)
        self.__department: str = deparment
        # self._planet: Planet = Planet(planet_info['planet_name'], planet_info['planet_type'])

class Soldier(Person):
    def __init__(self, name, age, planet_info) -> None:
        super().__init__(name)
        self.__age: int = 0
        
class Astarte(Person):
    def __init__(self, name, founding, planet_info) -> None:
        super().__init__(name)
        self.__founding: int = founding

class Primarch(Person):
    def __init__(self, name, alias) -> None:
        super().__init__(name)
        self.__alias: str = alias
        self.__loyalty: bool = None
        self.__status: str = ''
        self.__imperium: 'Imperium' = None

    def betray(self) -> bool:
        self.__loyalty = False
        print(f'Primarch {self._name} betrays the Emperor')
        return True
    
    def change_status(self, status) -> bool:
        self.__status = status
        return True

# _________________________________

class Segmentum():
    def __init__(self, name, location) -> None:
        self.__name: str = name
        self.__location: str = location
        self.__planets: List['Planet'] = []

    @property
    def name(self):
        return self.__name
    
    @property
    def planets(self):
        return self.__planets
    
    
    def add_planet(self, planet):
        self.__planets.append(planet)
        print(f'Added Planet {planet.name} to Segmentum {self.name}')
        return True

class Planet():
    def __init__(self, name, type) -> None:
        self.__name: str = name
        self.__type_: str = type
        self.__chapter: 'Chapter' = None
        self.__regiments: List['Regiment'] = []

    @property
    def name(self):
        return self.__name
    
    @property
    def chapter(self):
        return self.__chapter
    
    @chapter.setter
    def chapter(self, value):
        self.__chapter = value
        return True

class Regiment:
    def __init__(self, name, planet) -> None:
        self.__name: str = name
        self.__planet: str = planet
        self.__soldiers: List['Soldier'] = []
    
    @property
    def name(self):
        return self.__name
    
    @property
    def soldiers(self):
        return self.__soldiers
    
    def add_soldier(self, soldier: 'Soldier') -> bool:
        self.__soldiers.append(soldier)
        return True
    


class Chapter:
    def __init__(self, name, primarch, planet) -> None:
        self.__name: str = name
        self.__primarch: 'Primarch' = primarch
        self.__planet: 'Planet' = planet
        self.__astartes: List['Astarte'] = [name]
        self.__succesor_chapters: List['Chapter'] = []

    @property
    def name(self):
        return self.__name
    
    @property
    def primarch(self):
        return self.__primarch
    
    def add_successor_chapter(self, chapter: 'Chapter') -> bool:
        self.__succesor_chapters.append(chapter)
        print(f'Added Successor Chapter {chapter.name} to Chapter {self.name}')
        return True
    
    def add_astarte(self, astarte: 'Astarte'):
        self.__astartes.append(astarte)
        if len(self.__astartes) == 1000:
            print(f'Chapter {self.name} is full')
        if len(self.__astartes) == 1001:
            print('RuntimeError: There can only be 1000 Astartes per Chapter')
            return False
        return True

# _____________________________________________________

class Administratum:
    def __init__(self) -> None:
        self.__planet_registry: List[int] = []
        self.__bureaucrats: List['Bureaucrat'] = []

    def add_planet_registry(self, value) -> bool:
        self.__planet_registry.append(value)
        return True
    
    def add_bureaucrat(self, bureaucrat) -> bool:
        self.__bureaucrats.append(bureaucrat)
        return True

    @property
    def planet_registry(self):
        return self.__planet_registry
    
    @property
    def bureaucrats(self):
        return self.__bureaucrats

class AstraMilitarum:
    def __init__(self) -> None:
        self.__regiments: List['Regiment'] = []

    @property
    def regiments(self):
        return self.__regiments

class AdeptusAstartes:
    def __init__(self) -> None:
        self.__chapters: List['Chapter'] = []

    @property
    def chapters(self):
        return self.__chapters
    
