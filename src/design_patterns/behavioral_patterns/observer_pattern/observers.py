from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# Usamos TYPE_CHECKING para evitar importaciones circulares en tiempo de ejecución.
# El type hint 'Subject' solo es necesario para el análisis estático.
if TYPE_CHECKING:
    from .subjects import Subject


class Observer(ABC):
    """
    La interfaz Observer declara el método de actualización, que es utilizado
    por los sujetos para notificar a los observadores.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        ...


class TemperatureDisplay(Observer):
    """Observador Concreto: Muestra la temperatura actual."""

    def update(self, subject: Subject) -> None:
        print(f"Display de Temperatura: La nueva temperatura es {subject.temperature}°C")


class FanController(Observer):
    """Observador Concreto: Controla un ventilador basado en la temperatura."""

    def __init__(self, threshold: float):
        self._threshold = threshold

    def update(self, subject: Subject) -> None:
        if subject.temperature > self._threshold:
            print(f"Controlador del Ventilador: Temperatura ({subject.temperature}°C) por encima del umbral ({self._threshold}°C). ¡Encendiendo ventilador!")
        else:
            print(f"Controlador del Ventilador: Temperatura ({subject.temperature}°C) normal. Ventilador apagado.")