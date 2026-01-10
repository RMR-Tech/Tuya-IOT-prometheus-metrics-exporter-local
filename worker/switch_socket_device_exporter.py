import asyncio

from loguru import logger

from devices.switch_socket import SwitchSocketDevice
from metrics.switch_socket import update_switch_socket_metrics
from models.device.config.base import BaseDeviceConfig
from models.monitoring_data.switch_socket import SwitchSocketMonitoringData
from models.worker.base import BaseWorker


class SwitchSocketDeviceExporter(BaseWorker):
    def __init__(self, devices_configs: list[BaseDeviceConfig], time_sleep: float = 10) -> None:
        self.devices_configs = devices_configs
        self.devices: list[SwitchSocketDevice] = []
        self.running = True
        self.time_sleep = time_sleep

    def stop(self) -> None:
        self.running = False

    def run(self) -> None:
        raise NotImplementedError

    async def arun(self) -> None:
        logger.info("Starting Switch Socket Device Exporter")
        self.running = True
        await self._ainit_devices()

        logger.info("Switch Socket Device Exporter initialized")

        asyncio.create_task(self._arun())

    async def _arun(self) -> None:
        logger.info("Running Switch Socket Device Exporter")
        while self.running:
            for device in self.devices:
                monitoring_data = await device.aget_monitoring_data()
                update_switch_socket_metrics(
                    device.device_id,
                    device.name,
                    SwitchSocketMonitoringData(**monitoring_data.model_dump()),
                )

            await asyncio.sleep(self.time_sleep)

    async def _ainit_devices(self) -> None:
        for device_config in self.devices_configs:
            logger.info(f"Initializing device: {device_config.name}")
            device = SwitchSocketDevice(
                device_id=device_config.id,
                device_key=device_config.key,
                name=device_config.name,
                device_ip=device_config.ip,
            )
            await device.ainit()
            logger.info(f"Device initialized: {device_config.name}")
            self.devices.append(device)
