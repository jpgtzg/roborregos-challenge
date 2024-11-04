# Written by Juan Pablo Gutiérrez

from abc import ABC, abstractmethod
import time

class ActionInterface(ABC):
    def __init__(self, name):
        self.name = name
        self.requirements = set()

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def is_finished(self) -> bool:
        return False
    
    @abstractmethod
    def end(self, interrupted: bool):
        pass

