from typing import List, Union
from models.coord import Coord
from models.enum import Gender


class Individual:
    '''對像類別'''
    ttl_ids = []

    def __init__(self, id: int, gender: Gender, age: int, coord: Coord, intro: str = "", habits: Union[str, List[str]] = "", prefer_different: bool = False):
        if not isinstance(id, int):
            raise ValueError(
                f"Incorrect id type, Except `int`, but got {type(id)}")
        if id in self.ttl_ids:
            raise ValueError(f"Individual id {id} already exists")
        self.__id: int = id
        self.ttl_ids.append(id)
        self.gender = gender
        self.age: int = age
        self.intro: str = intro
        self.habits: Union[str, List[str]] = habits
        self.coord: Coord = coord
        self.prefer_different: bool = prefer_different

    def __str__(self):
        return f"Individual(id={self.id},gender={self.gender},age={self.age},intro={self.intro},habits={self.habits},coord={self.coord},prefer_different={self.prefer_different})"

    def __repr__(self):
        return f"Individual(id={self.id},gender={self.gender},age={self.age},intro={self.intro},habits={self.habits},coord={self.coord},prefer_different={self.prefer_different})"

    @property
    def id(self):
        return self.__id

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value: Gender):
        if not isinstance(value, Gender):
            raise ValueError(
                f"Incorrect gender type, Except `Gender` Enum, but got {type(value)}")
        self.__gender = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if not isinstance(value, int):
            raise ValueError(
                f"Incorrect age type, Except `int`, but got {type(value)}")
        if value < 0:
            raise ValueError("Age should be positive")
        if value < 18:
            raise ValueError("Age should be at least 18")
        self.__age = value

    @property
    def intro(self):
        return self.__intro

    @intro.setter
    def intro(self, value: str):
        if not isinstance(value, str):
            raise ValueError(
                f"Incorrect intro type, Except `str`, but got {type(value)}")
        if len(value) > 200:
            raise ValueError("Introduction should be at most 200 characters")
        self.__intro = value

    @property
    def habits(self):
        return self.__habits

    @habits.setter
    def habits(self, value: Union[str, List[str]]):
        if isinstance(value, str):
            value = value.split(",")
        if not isinstance(value, list):
            raise ValueError(
                f"Incorrect habits type, Except `list`, but got {type(value)}")
        for habit in value:
            if len(habit) > 10:
                raise ValueError("Per Habit should be at most 10 characters")
        self.__habits = value

    @property
    def coord(self):
        return self.__coord

    @coord.setter
    def coord(self, value: Coord):
        if not isinstance(value, Coord):
            raise ValueError(
                f"Incorrect coord type, Except `Coord`, but got {type(value)}")
        self.__coord = value

    @property
    def prefer_different(self):
        return self.__prefer_different

    @prefer_different.setter
    def prefer_different(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError(
                f"Incorrect prefer_different type, Except `bool`, but got {type(value)}")
        self.__prefer_different = value
