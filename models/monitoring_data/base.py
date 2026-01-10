from typing import Any

from pydantic import BaseModel


class BaseMonitoringData(BaseModel):
    """
    Base model for monitoring data.
    """

    def get_label_list(self) -> list[str]:
        """
        Get the label list for the monitoring data.
        """
        # Access model_fields from the class, not the instance
        return list(self.__class__.model_fields.keys())

    def get_value_list(self) -> list[Any]:
        """
        Get the value list for the monitoring data.
        """
        return [getattr(self, field) for field in self.get_label_list()]
