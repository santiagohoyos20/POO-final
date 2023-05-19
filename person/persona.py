from __future__ import annotations
from abc import ABC
from typing import List

from utils.enums import Status


class Person(ABC):
    ID = 0
    def __init__(self, name) -> None:
        self._id_string: str = format(Person.ID, '06x')
        self._name: str = name + ' ' + self._id_string
        self._planet: 'Planet' = None

        Person.ID += 1

    @property
    def id_string(self) -> str:
        return self._id_string

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def planet(self) -> 'Planet':
        return self._planet
    
    @planet.setter
    def planet(self, value: 'Planet') -> bool:
        self._planet = value
        return True
    
class Bureaucrat(Person):
    def __init__(self, name, deparment, planet_info) -> None:
        super().__init__(name)
        self.__department: str = deparment
        Person.ID += 1

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
        self.__loyalty: bool = True
        self.__status = Status.ALIVE.value
        self.__imperium: 'Imperium' = None

    @property
    def alias(self) -> str:
        return self.__alias
    
    @property
    def loyalty(self) -> bool:
        return self.__loyalty

    @property
    def status(self) -> str:
        return self.__status

    def betray(self) -> bool:
        self.__loyalty = False
        print(f'Primarch {self._name[:-7]} betrays the Emperor')
        return True
    
    def change_status(self, status) -> bool:
        self.__status = status.value
        return True

