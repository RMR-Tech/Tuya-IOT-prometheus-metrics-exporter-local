from abc import ABC, abstractmethod


class BaseWorker(ABC):
    running: bool = True

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def arun(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> None:
        raise NotImplementedError
