'''配對系統單元測試'''
import pytest

from models.coord import Coord
from models.enum import Gender
from models.individual import Individual
from models.matchmaking_system import MatchmakingSystem
from models.strategy import DistanceBasedStrategy, HabitBasedStrategy


def test_main():
    print()
    individual_list = []
    individual_list.append(Individual(id=1, gender=Gender.MALE, age=18,
                                      coord=Coord(0, 0), intro="",
                                      habits="動漫,科技", prefer_different=False))
    individual_list.append(Individual(id=2, gender=Gender.MALE, age=20,
                                      coord=Coord(10, 5), intro="",
                                      habits="爬山,凹豆", prefer_different=False))
    individual_list.append(Individual(id=3, gender=Gender.FEMALE, age=25,
                                      coord=Coord(20, 15), intro="",
                                      habits="凹豆,科技", prefer_different=False))
    strategy = HabitBasedStrategy()
    system = MatchmakingSystem(strategy, individual_list)
    system.start()
    matched_individuals = system.export_data()
    for key, value in matched_individuals.items():
        print(
            f"Individual {key.id} {key.habits} match {value.id} {value.habits}")
    assert matched_individuals[individual_list[0]].id == 3
    assert matched_individuals[individual_list[1]].id == 3
    assert matched_individuals[individual_list[2]].id == 1

    strategy = DistanceBasedStrategy()
    system.strategy = strategy
    system.start()
    matched_individuals = system.export_data()
    for key, value in matched_individuals.items():
        print(
            f"Individual {key.id} {key.habits} match {value.id} {value.habits}")
    assert matched_individuals[individual_list[0]].id == 2
    assert matched_individuals[individual_list[1]].id == 1
    assert matched_individuals[individual_list[2]].id == 2

    individual_list.append(Individual(id=4, gender=Gender.FEMALE, age=25,
                                      coord=Coord(100, 150), intro="",
                                      habits="凹豆,美術", prefer_different=True))
    strategy = HabitBasedStrategy()
    system = MatchmakingSystem(strategy, individual_list)
    system.start()
    matched_individuals = system.export_data()
    for key, value in matched_individuals.items():
        print(
            f"Individual {key.id} {key.habits} match {value.id} {value.habits}")
    assert matched_individuals[individual_list[0]].id == 3
    assert matched_individuals[individual_list[1]].id == 3
    assert matched_individuals[individual_list[2]].id == 1
    assert matched_individuals[individual_list[3]].id == 1

    strategy = DistanceBasedStrategy()
    system.strategy = strategy
    system.start()
    matched_individuals = system.export_data()
    for key, value in matched_individuals.items():
        print(
            f"Individual {key.id} {key.habits} match {value.id} {value.habits}")
    assert matched_individuals[individual_list[0]].id == 2
    assert matched_individuals[individual_list[1]].id == 1
    assert matched_individuals[individual_list[2]].id == 2
    assert matched_individuals[individual_list[3]].id == 1
