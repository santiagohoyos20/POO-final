from __future__ import annotations
from abc import ABC
from typing import List, Optional, Tuple

# from emperor import Imperium
# from clases import Planet

import emperor
import clases


class Person(ABC):
    def __init__(self, name) -> None:
        self._id_string: str = ''
        self._name: str = name
        self.__planet: 'Planet' = None

class Bureaucrat(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.__department: str = ''

class Soldier(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.__age: int = 0
        
class Astarte(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.__founding: int = 0


class Primarch(Person):
    def __init__(self) -> None:
        self.__alias: str = ''
        self.__loyalty: bool = None
        self.__status: str = ''
        self.__imperium: 'Imperium' = None

