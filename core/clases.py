from __future__ import annotations
from abc import ABC
from typing import List, Dict

import persona

class Sementum():
    def __init__(self, name, location) -> None:
        self.__name: str = name
        self.__location: str = location
        self.__planets: List['Planet'] = []

class Planet():
    def __init__(self, name, type) -> None:
        self.__name: str = name
        self.__type_: str = type
        self.__chapter: 'Chapter' = None
        self.__regiments: List['Regiment'] = []

class Regiment:
    def __init__(self, name, planet) -> None:
        self.__name: str = name
        self.__planet: 'Planet' = planet
        self.__soldiers: List['Soldier'] = []

class Chapter:
    def __init__(self, name, primarch, planet) -> None:
        self.__name: str = name
        self.__primarch: 'Primarch' = primarch
        self.__planet: 'Planet' = planet
        self.__astartes: List['Astarte'] = [name]
        self.__succesor_chapters: List['Chapter'] = []
        
        
        

        
        
