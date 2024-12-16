from abc import ABC, abstractmethod
from typing import List

from models.individual import Individual


class IStrategy(ABC):
    '''策略介面'''

    def __init__(self):
        super().__init__()

    @abstractmethod
    def match(self, individual: Individual, other_individuals: List[Individual]):
        '''配對對像與其他對像的抽象方法'''
        pass
