from pydantic import Field

from .base import BaseMonitoringData


class SwitchSocketMonitoringData(BaseMonitoringData):
    """
    Monitoring data for a switch outlet.
    """

    switch_position_status: bool | None = Field(None, description="The position of the switch")
    current_amperes: float = Field(..., description="The current of the outlet in Amperes")
    power_watts: float = Field(..., description="The power of the outlet in Watts")
    voltage_volts: float = Field(..., description="The voltage of the outlet in Volts")

    power_on_stage_setting: str = Field(..., description="The power on stage setting of the outlet")
    overcharge_switch: bool = Field(..., description="The overcharge switch of the outlet")
    indicator_status_setting: str = Field(
        ..., description="The indicator status setting of the outlet"
    )
