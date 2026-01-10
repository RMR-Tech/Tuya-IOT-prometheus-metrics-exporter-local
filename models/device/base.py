from abc import ABC, abstractmethod

from models.monitoring_data.base import BaseMonitoringData


class BaseDevice(ABC):
    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def aget_monitoring_data(self) -> BaseMonitoringData:
        raise NotImplementedError

    @abstractmethod
    def get_monitoring_data(self) -> BaseMonitoringData:
        raise NotImplementedError

    @abstractmethod
    def init(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def ainit(self) -> None:
        raise NotImplementedError
