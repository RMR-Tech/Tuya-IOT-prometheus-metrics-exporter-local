from models.device.config.base import BaseDeviceConfig

SOCKET_PLUG_DEVICES: list[BaseDeviceConfig] = [
    BaseDeviceConfig(
        id="DEVICE_ID",
        ip="Auto",
        key="DEVICE_KEY",
        name="DEVICE_NAME",
    ),
]
