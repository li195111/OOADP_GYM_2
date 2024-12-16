'''興趣先決配對策略'''

from typing import List

from models.individual import Individual
from models.strategy.base import IStrategy


class HabitBasedStrategy(IStrategy):
    '''興趣先決配對策略'''

    def __init__(self):
        super().__init__()

    def match(self, individual: Individual, other_individuals: List[Individual]):
        '''配對對像與其他對像的方法,

        偏好認識不同的人 -> 交集最少的, 偏好認識相同的人 -> 交集最多的
        Args:
            individual (Individual): 配對對像
            other_individuals (List[Individual]): 其他對像列表
        Returns:
            Individual: 配對結果
        '''
        print('偏好認識興趣相同的人: ', individual.prefer_different)
        match_fn = min if individual.prefer_different else max
        individual_habits_set = set(individual.habits)
        other_habits_set_intersection_list = []
        for other_individual in other_individuals:
            other_intersection_set = individual_habits_set.intersection(
                set(other_individual.habits))
            other_habits_set_intersection_list.append(
                len(other_intersection_set))
        if not other_habits_set_intersection_list:
            raise ValueError("No other individuals data to match")
        match_intersection_value = match_fn(other_habits_set_intersection_list)
        match_intersection_index = other_habits_set_intersection_list.index(
            match_intersection_value)
        return other_individuals[match_intersection_index]
