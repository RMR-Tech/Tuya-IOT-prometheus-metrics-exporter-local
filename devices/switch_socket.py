import asyncio

import tinytuya
from loguru import logger

from models.device.base import BaseDevice
from models.monitoring_data.base import BaseMonitoringData
from models.monitoring_data.switch_socket import SwitchSocketMonitoringData


class SwitchSocketDevice(BaseDevice):
    def __init__(
        self,
        device_id: str,
        device_key: str,
        name: str = "",
        device_ip: str = "Auto",
    ) -> None:
        self.device_id = device_id
        self.device_key = device_key
        self.device_ip = device_ip
        self.name = name
        self.device: tinytuya.OutletDevice | None = None

        if self.name == "":
            self.name = f"Switch Socket {self.device_id}"

    def get_name(self) -> str:
        return self.name

    def init(self) -> None:
        logger.info(f"Initializing device: {self.device_id} {self.device_ip} {self.name}")
        self.device = tinytuya.OutletDevice(
            self.device_id, self.device_ip, self.device_key, persist=True
        )
        logger.info(f"Device initialized: {self.device_id} {self.device_ip} {self.name}")

    async def ainit(self) -> None:
        await asyncio.to_thread(self.init)

    async def aget_monitoring_data(self) -> BaseMonitoringData:
        if self.device is None:
            await self.ainit()

        status_dict = await self._aget_device_status_dict()
        if "dps" not in status_dict:
            logger.error(f"Device status dictionary does not contain 'dps' key: {status_dict}")
            raise ValueError("Device status dictionary does not contain 'dps' key")

        return self._parse_status_dps_to_monitoring_data(status_dict["dps"])

    def get_monitoring_data(self) -> BaseMonitoringData:
        if self.device is None:
            self.init()

        status_dict = self._get_device_status_dict()
        if "dps" not in status_dict:
            logger.error(f"Device status dictionary does not contain 'dps' key: {status_dict}")
            raise ValueError("Device status dictionary does not contain 'dps' key")

        return self._parse_status_dps_to_monitoring_data(status_dict["dps"])

    def _get_device_status_dict(self) -> dict:
        if self.device is None:
            self.init()

        return self.device.status()  # type: ignore

    async def _aget_device_status_dict(self) -> dict:
        if self.device is None:
            await self.ainit()

        return await asyncio.to_thread(self.device.status)  # type: ignore

    def _parse_status_dps_to_monitoring_data(self, status_dps: dict) -> SwitchSocketMonitoringData:
        logger.debug(f"Parsing status DPS to monitoring data: {status_dps}")

        return SwitchSocketMonitoringData(
            switch_position_status=status_dps.get("1"),
            current_amperes=float(status_dps.get("18", 0)) / 1000.0,
            power_watts=float(status_dps.get("19", 0)) / 10.0,
            voltage_volts=float(status_dps.get("20", 0)) / 10.0,
            power_on_stage_setting=status_dps.get("38", "unknown"),
            overcharge_switch=bool(status_dps.get("39", False)),
            indicator_status_setting=status_dps.get("40", "unknown"),
        )
