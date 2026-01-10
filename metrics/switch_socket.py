"""
Prometheus metrics for switch socket devices.
"""

from prometheus_client import Gauge, Info

from models.monitoring_data.switch_socket import SwitchSocketMonitoringData

# Switch Socket Metrics
switch_socket_switch_state = Gauge(
    "tuya_switch_socket_switch_state",
    "Switch position status (1=ON, 0=OFF)",
    ["device_id", "device_name"],
)

switch_socket_current_amperes = Gauge(
    "tuya_switch_socket_current_amperes",
    "Current consumption in Amperes",
    ["device_id", "device_name"],
)

switch_socket_power_watts = Gauge(
    "tuya_switch_socket_power_watts",
    "Power consumption in Watts",
    ["device_id", "device_name"],
)

switch_socket_voltage_volts = Gauge(
    "tuya_switch_socket_voltage_volts",
    "Voltage in Volts",
    ["device_id", "device_name"],
)

switch_socket_overcharge_protection = Gauge(
    "tuya_switch_socket_overcharge_protection",
    "Overcharge protection enabled (1=enabled, 0=disabled)",
    ["device_id", "device_name"],
)

switch_socket_info = Info(
    "tuya_switch_socket",
    "Switch socket device information and settings",
    ["device_id", "device_name"],
)


def update_switch_socket_metrics(
    device_id: str,
    device_name: str,
    monitoring_data: SwitchSocketMonitoringData,
) -> None:
    """
    Update Prometheus metrics for a switch socket device.

    Args:
        device_id: The unique device identifier
        device_name: The human-readable device name
        monitoring_data: The monitoring data from the device
    """
    labels = {"device_id": device_id, "device_name": device_name}

    # Update numerical gauges
    switch_socket_current_amperes.labels(**labels).set(monitoring_data.current_amperes)
    switch_socket_power_watts.labels(**labels).set(monitoring_data.power_watts)
    switch_socket_voltage_volts.labels(**labels).set(monitoring_data.voltage_volts)

    # Update switch state (convert bool to int)
    if monitoring_data.switch_position_status is not None:
        switch_socket_switch_state.labels(**labels).set(
            1 if monitoring_data.switch_position_status else 0
        )

    # Update overcharge protection
    switch_socket_overcharge_protection.labels(**labels).set(
        1 if monitoring_data.overcharge_switch else 0
    )

    # Update info metric with settings
    switch_socket_info.labels(**labels).info(
        {
            "power_on_stage_setting": monitoring_data.power_on_stage_setting,
            "indicator_status_setting": monitoring_data.indicator_status_setting,
        }
    )
