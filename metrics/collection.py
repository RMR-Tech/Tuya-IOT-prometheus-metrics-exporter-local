"""
Prometheus metrics collection and exposition for FastAPI.
"""

from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest
from starlette.requests import Request
from starlette.responses import Response

# Collection metrics
tuya_metrics_collection_total = Counter(
    "tuya_metrics_collection_total",
    "Total number of metrics collections",
    ["device_id", "device_name", "device_type"],
)

tuya_metrics_collection_errors_total = Counter(
    "tuya_metrics_collection_errors_total",
    "Total number of errors during metrics collection",
    ["device_id", "device_name", "device_type", "error_type"],
)


def record_collection_success(
    device_id: str,
    device_name: str,
    device_type: str,
) -> None:
    """
    Record a successful metrics collection.

    Args:
        device_id: The unique device identifier
        device_name: The human-readable device name
        device_type: The type of device
    """
    tuya_metrics_collection_total.labels(
        device_id=device_id,
        device_name=device_name,
        device_type=device_type,
    ).inc()


def record_collection_error(
    device_id: str,
    device_name: str,
    device_type: str,
    error_type: str,
) -> None:
    """
    Record a metrics collection error.

    Args:
        device_id: The unique device identifier
        device_name: The human-readable device name
        device_type: The type of device
        error_type: The type of error that occurred
    """
    tuya_metrics_collection_errors_total.labels(
        device_id=device_id,
        device_name=device_name,
        device_type=device_type,
        error_type=error_type,
    ).inc()


async def metrics_handler(request: Request) -> Response:
    """
    FastAPI endpoint handler for Prometheus metrics.

    Args:
        request: The FastAPI request object

    Returns:
        Response with Prometheus metrics in text format
    """
    metrics_output = generate_latest()
    return Response(content=metrics_output, media_type=CONTENT_TYPE_LATEST)
