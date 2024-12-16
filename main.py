from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from pathlib import Path
from dataclasses import dataclass
from enum import Enum

class MatchmakingSystem:

    def __init__(self, strategy: Strategy, data_path: str):
        self.strategy = strategy
        self.data_path = Path(data_path)
        self.individual_data: List[Individual] = []
        self.individual_match_results: List[Individual] = []

    def load_data(self):
        if not self.data_path.exists():
            raise FileNotFoundError("Data file not found")
        self.individual_data = self.data_path.read_text().split("\n")
        

    def use_strategy(self):
        self.individual_match_results.clear()
        for individual in self.individual_data:
            exclude_data = self.individual_data.copy()
            exclude_data.remove(individual)
            match_result = self.strategy.match(individual, exclude_data)
            self.individual_match_results.append(match_result)

    def export_data(self):
        return self.individual_match_results

class Gender(Enum):
    MALE = '男生'
    FEMALE = '女生'

@dataclass
class Coord:
    x: float
    y: float

@dataclass
class Individual:
    id: int
    gender: Gender
    age: int
    intro: str
    habits: List[str]
    coord: Coord
    prefer_different: bool = False

    def __post_init__(self):
        if self.age < 18:
            raise ValueError("Age should be at least 18")
        if len(self.habits) < 3:
            raise ValueError("At least 3 habits should be provided")
        if len(self.intro) < 10:
            raise ValueError("Introduction should be at least 10 characters")

class Strategy(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def match(self):
        pass


class HabitBasedStrategy(Strategy):

    def __init__(self):
        pass

    def match(self, individual: Individual, other_individuals: List[Individual]):
        pass

class DistanceBasedStrategy(Strategy):

    def __init__(self):
        pass

    def match(self, individual: Individual, other_individuals: List[Individual]):
        pass
