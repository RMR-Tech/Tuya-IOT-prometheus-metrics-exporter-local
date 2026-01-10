from devices.switch_socket import SwitchSocketDevice

socket_dev_1 = SwitchSocketDevice(
    device_id="DEVICE_ID",
    device_key="DEVICE_KEY",
    name="Device 1",
)

socket_dev_1.init()
print(socket_dev_1.get_monitoring_data())
