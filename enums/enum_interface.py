import abc
from typing import List


class EnumInterface(metaclass=abc.ABCMeta):

    @classmethod
    @abc.abstractmethod
    def info(cls) -> str:
        pass

    @staticmethod
    @abc.abstractmethod
    def additional_parameters() -> List:
        pass