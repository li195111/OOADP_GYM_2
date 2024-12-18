from models.coord import Coord
from models.enum import Gender
from models.individual import Individual
from models.matchmaking_system import MatchmakingSystem
from models.strategy import DistanceBasedStrategy, HabitBasedStrategy


def main():
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
    for individual in individual_list:
        print(individual)
    print('興趣先決配對')
    strategy = HabitBasedStrategy()
    system = MatchmakingSystem(strategy, individual_list)
    system.start()
    for key, value in system.export_data().items():
        print(
            f"Individual {key.id} {key.habits} match {value.id} {value.habits}")
    print('距離先決配對')
    strategy = DistanceBasedStrategy()
    system.strategy = strategy
    system.start()
    for key, value in system.export_data().items():
        print(
            f"Individual {key.id} {key.coord} match {value.id} {value.coord}")

    individual_list.append(Individual(id=4, gender=Gender.FEMALE, age=25,
                                      coord=Coord(100, 150), intro="",
                                      habits="凹豆,美術", prefer_different=True))
    print('興趣先決配對')
    strategy = HabitBasedStrategy()
    system = MatchmakingSystem(strategy, individual_list)
    system.start()
    for key, value in system.export_data().items():
        print(
            f"Individual {key.id} {key.habits} match {value.id} {value.habits}")
    print('距離先決配對')
    strategy = DistanceBasedStrategy()
    system.strategy = strategy
    system.start()
    for key, value in system.export_data().items():
        print(
            f"Individual {key.id} {key.habits} match {value.id} {value.habits}")


if __name__ == "__main__":
    main()
