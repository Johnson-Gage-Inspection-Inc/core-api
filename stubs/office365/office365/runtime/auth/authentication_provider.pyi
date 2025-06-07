import abc
from abc import ABCMeta, abstractmethod

class AuthenticationProvider(metaclass=abc.ABCMeta):
    __metaclass__ = ABCMeta
    @abstractmethod
    def authenticate_request(self, request): ...
