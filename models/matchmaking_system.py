'''配對系統'''


from typing import Dict, List

from models.individual import Individual
from models.strategy.base import IStrategy


class MatchmakingSystem:
    '''配對系統類別

    系統會幫每位用戶配對最適合他的用戶
    '''

    def __init__(self, strategy: IStrategy, individual_data: List[Individual]):
        self.strategy = strategy
        self.individual_data: List[Individual] = individual_data
        self.individual_match_results: Dict[Individual, Individual] = {}

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, value: IStrategy):
        if not isinstance(value, IStrategy):
            raise ValueError(
                f"Incorrect strategy type, Except `Strategy`, but got {type(value)}")
        self.__strategy = value

    def start(self):
        '''開始配對'''
        self.use_strategy()

    def use_strategy(self):
        '''使用策略進行配對'''
        self.individual_match_results.clear()
        for individual in self.individual_data:
            exclude_data = self.individual_data.copy()
            exclude_data.remove(individual)
            match_result = self.strategy.match(individual, exclude_data)
            self.individual_match_results[individual] = match_result

    def export_data(self):
        '''匯出配對結果'''
        return self.individual_match_results
