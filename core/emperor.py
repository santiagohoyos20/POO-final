from __future__ import annotations
from typing import List, Optional, Tuple, Dict

from person.persona import *
from utils.enums import PlanetType, decimal_to_roman

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
        new_primarch.planet = new_planet
        print(f'The Emperor created Primarch {nombre}')
        return True
    
class Imperium:
    __instance = None  # Private instance variable

    @staticmethod
    def get_instance() -> 'Imperium':
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
    
    @property
    def planet(self) -> 'Planet':
        return self.__planet
    
    def add_segmentum(self, segmentum: 'Segmentum') -> bool:
        self.__segmentums.append(segmentum)
        print(f'Added Segmentum {segmentum.name} to the Imperium')
        return True

    def add_primarch(self, value: 'Primarch') -> bool:
        self.__primarchs.append(value)
        return True

    def add_bureaucrat(self, bureaucrat: 'Bureaucrat') -> bool:
        self.__administratum.add_planet_registry(0)
        self.__administratum.add_bureaucrat(bureaucrat)
        print(f'{bureaucrat.name} started to work at Imperium')
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
    
    def add_chapter(self, name, primarch, planet) -> bool:
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
    
    def get_chapter(self, index) -> 'Chapter':
        return self.__adeptus_astartes.chapters[index]
    
    def add_regiment(self, name, planet: str) -> bool:
        for s in self.segmentums:
            for p in s.planets:
                if p.name == planet:
                    planet = p
        new_regiment = Regiment(name, planet)
        self.__astra_militarum.regiments.append(new_regiment)
        planet.regiments.append(new_regiment)
        print(f'Created Regiment {new_regiment.name} of Astra Militarum')
        return True
    
    def get_regiment(self, index) -> 'Regiment':
        return self.__astra_militarum.regiments[index]
    
    def bureaucrat_max_registry(self) -> List:
        result = []
        r_max = 0
        index_max = 0
        c = 0
        for r in self.__administratum.planet_registry: 
            if r >= r_max:
                r_max = r
                index_max = c
            c += 1

        result.append(self.__administratum.bureaucrats[index_max])
        result.append(self.__administratum.planet_registry[index_max])
        return result
    
    def planet_type_quantity(self) -> bool:
        result = {
            PlanetType.AGRI : 0,
            PlanetType.CIVILISED : 0,
            PlanetType.DAEMON : 0,
            PlanetType.DEAD : 0,
            PlanetType.DEATH : 0,
            PlanetType.FERAL : 0,
            PlanetType.FEUDAL : 0,
            PlanetType.FORGE : 0,
            PlanetType.FRONTIER : 0,
            PlanetType.HIVE : 0,
        }
        for s in self.__segmentums:
            for p in s.planets:
                for key, value in result.items():
                    if p.type_ == key:
                        result[key] = value + 1
                        break

        print(
f'''---------- Planet Type ----------
- Agri Planet Quantity = {result[PlanetType.AGRI]}
- Civilised Planet Quantity = {result[PlanetType.CIVILISED ]}
- Daemon Planet Quantity = {result[PlanetType.DAEMON]}
- Dead Planet Quantity = {result[PlanetType.DEAD]}
- Death Planet Quantity = {result[PlanetType.DEATH]}
- Feral Planet Quantity = {2}
- Feudal Planet Quantity = {result[PlanetType.FEUDAL]}
- Forge Planet Quantity = {1}
- Frointer Planet Quantity = {result[PlanetType.FRONTIER]}
- Hive Planet Quantity = {3}'''
        )
        print()
        return True
    
    def show_primarchs_summary(self) -> bool:
        print('---------- Primarchs Summary ----------')
        c = 1
        for pm in self.__primarchs:
            total_soldiers = 0
            AAC = ''
            print('- Primarch', decimal_to_roman(c))
            if pm == None:
                print('  - Purged from Imperial Registry')
                print()
                c += 1
                continue          
            for s in self.segmentums:
                for p in s.planets:
                    if p.name == pm.planet.name:
                        planet = p
            
            for r in planet.regiments:
                total_soldiers += len(r.soldiers)

            for ch in self.__adeptus_astartes.chapters:
                if ch.primarch.name == pm.name:
                    AAC = ch.name
                    break

            print(f'''  - ID: {pm.id_string}
  - Name: {pm.name[:-7]}
  - Alias: {pm.alias}
  - Loyal: {pm.loyalty}
  - Status: {pm.status}
  - Planet: {pm.planet.name}
    - Astra Militarum Regiments Quantity: {len(planet.regiments)}
    - Astra Militarum Total Soldiers: {total_soldiers}
    - Adeptus Astates Chapter: {AAC}
      - Successor Chapters:''')
            c += 1
            for ch in self.__adeptus_astartes.chapters:
                if ch.primarch.name == pm.name:
                    if len(ch.succesor_chapters) == 0:
                        break
                    else:
                        for sc in ch.succesor_chapters:
                            print(f'        - {sc.name}')
            print()                   
        return True


class Segmentum:
    def __init__(self, name, location) -> None:
        self.__name: str = name
        self.__location: str = location
        self.__planets: List['Planet'] = []

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def planets(self) -> List['Planet']:
        return self.__planets
    
    
    def add_planet(self, planet: 'Planet') -> bool:
        self.__planets.append(planet)
        print(f'Added Planet {planet.name} to Segmentum {self.name}')
        return True

class Planet:
    def __init__(self, name, type) -> None:
        self.__name: str = name
        self.__type_: str = type
        self.__chapter: 'Chapter' = None
        self.__regiments: List['Regiment'] = []

    @property
    def name(self):
        return self.__name
    
    @property
    def type_(self):
        return self.__type_
    
    @property
    def chapter(self):
        return self.__chapter
    
    @chapter.setter
    def chapter(self, value):
        self.__chapter = value
        return True
    
    @property
    def regiments(self):
        return self.__regiments

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
    def succesor_chapters(self):
        return self.__succesor_chapters
    
    @property
    def primarch(self):
        return self.__primarch
    
    def add_successor_chapter(self, chapter: 'Chapter') -> bool:
        self.__succesor_chapters.append(chapter)
        print(f'Added Successor Chapter {chapter.name} to Chapter {self.name}')
        return True
    
    def add_astarte(self, astarte: 'Astarte')  -> bool:
        self.__astartes.append(astarte)
        if len(self.__astartes) == 1000:
            print(f'Chapter {self.name} is full')
        if len(self.__astartes) == 1001:
            print('RuntimeError: There can only be 1000 Astartes per Chapter')
            return False
        return True

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
