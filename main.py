import asyncio
import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

from config.device_config import SOCKET_PLUG_DEVICES
from metrics.collection import metrics_handler
from mylogging import logger
from worker.switch_socket_device_exporter import SwitchSocketDeviceExporter


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager to run worker loop during app lifetime"""
    # Startup: Initialize and start the worker
    worker = SwitchSocketDeviceExporter(SOCKET_PLUG_DEVICES)
    worker_task = asyncio.create_task(worker.arun())

    yield

    # Shutdown: Stop the worker gracefully
    worker.stop()
    await worker_task


app = FastAPI(title="Tuya Metrics Exporter", lifespan=lifespan)


@app.get("/ping", response_class=PlainTextResponse)
async def ping():
    """Simple ping endpoint that returns 'pong'"""
    return "pong"


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "service": "tuya-metrics-exporter"}


@app.get("/metrics")
async def metrics(request: Request):
    """Prometheus metrics endpoint"""
    return await metrics_handler(request)


def _init_example_device_config() -> None:
    # check if the .config folder exists and has device_config.py file
    if not os.path.exists(".config"):
        os.makedirs(".config")
    if not os.path.exists(".config/device_config.py"):
        with open(".config/device_config.py", "w") as f:
            f.write(
                "from models.device.config.base import BaseDeviceConfig\n\nSOCKET_PLUG_DEVICES: list[BaseDeviceConfig] = []"
            )


def main():
    _init_example_device_config()

    logger.info("Starting Tuya Metrics Exporter")
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
