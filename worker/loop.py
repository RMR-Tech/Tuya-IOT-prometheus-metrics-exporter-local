from config.device_config import SOCKET_PLUG_DEVICES
from worker.switch_socket_device_exporter import SwitchSocketDeviceExporter


async def loop() -> None:
    switch_socket_device_exporter = SwitchSocketDeviceExporter(SOCKET_PLUG_DEVICES)
    await switch_socket_device_exporter.arun()
