'''距離先決配對策略'''

from typing import List

from models.individual import Individual
from models.strategy.base import IStrategy


class DistanceBasedStrategy(IStrategy):
    '''距離先決配對策略'''

    def __init__(self):
        super().__init__()

    def match(self, individual: Individual, other_individuals: List[Individual]):
        '''配對對像與其他對像的方法,

        偏好認識不同的人 -> 距離最遠的, 偏好認識相同的人 -> 距離最近的
        Args:
            individual (Individual): 配對對像
            other_individuals (List[Individual]): 其他對像列表
        Returns:
            Individual: 配對結果
        '''
        print('偏好認識遠距的人: ', individual.prefer_different)
        match_fn = max if individual.prefer_different else min
        individual_coord = individual.coord
        other_coords_distance_list = []
        for other_individual in other_individuals:
            other_coord = other_individual.coord
            distance = ((individual_coord.x - other_coord.x) **
                        2 + (individual_coord.y - other_coord.y) ** 2) ** 0.5
            other_coords_distance_list.append(distance)
        if not other_coords_distance_list:
            raise ValueError("No other individuals data to match")
        match_intersection_value = match_fn(other_coords_distance_list)
        match_intersection_index = other_coords_distance_list.index(
            match_intersection_value)
        return other_individuals[match_intersection_index]
