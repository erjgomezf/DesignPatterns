from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .observers import Observer


class Subject(ABC):
    """
    La interfaz Subject declara un conjunto de métodos para gestionar suscriptores.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Adjunta un observador al sujeto."""
        ...

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Desadjunta un observador del sujeto."""
        ...

    @abstractmethod
    def notify(self) -> None:
        """Notifica a todos los observadores sobre un evento."""
        ...


class WeatherStation(Subject):
    """
    El Sujeto Concreto posee algún estado importante y notifica a los
    observadores cuando el estado cambia.
    """

    _temperature: float = 0.0
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print(f"WeatherStation: Se ha suscrito un nuevo observador: {observer.__class__.__name__}")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("WeatherStation: Notificando a todos los observadores...")
        for observer in self._observers:
            observer.update(self)

    def set_temperature(self, temp: float) -> None:
        """
        Método de negocio que cambia el estado y notifica a los observadores.
        """
        self._temperature = temp
        print(f"WeatherStation: La temperatura ha cambiado a {self._temperature}°C.")
        self.notify()

    @property
    def temperature(self) -> float:
        return self._temperature